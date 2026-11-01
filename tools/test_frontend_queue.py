"""Maintainer checks: frontend automation must never mutate core issues."""
import copy
import unittest
from unittest.mock import patch

import frontend_queue as queue
from learning_queue import issue_key


class FakeGitHub:
    def __init__(self):
        self.issues = [{"number": 1, "title": "Learner 01 | Day 001: Python", "body": "Keep this exact issue.",
                        "state": "open", "assignees": [{"login": "PratikTalware26"}], "labels": [{"name": "queue-current"}]}]
        self.mutations = []

    def __call__(self, *args, payload=None):
        endpoint = args[1]
        if payload is None:
            items = self.issues if 'state=all' in endpoint else [i for i in self.issues if i['state'] == 'open']
            return [copy.deepcopy(items)]
        self.mutations.append((endpoint, copy.deepcopy(payload)))
        if args[-1] == 'POST':
            item = {"number": len(self.issues) + 500, "state": "open", "state_reason": None, **copy.deepcopy(payload)}
            self.issues.append(item)
        else:
            number = int(endpoint.rsplit('/', 1)[1])
            if number == 1:
                raise AssertionError('Core issue mutation attempted')
            item = next(i for i in self.issues if i['number'] == number)
            item.update(copy.deepcopy(payload))
        if 'labels' in payload:
            item['labels'] = [{'name': n} for n in payload['labels']]
        if 'assignees' in payload:
            item['assignees'] = [{'login': n} for n in payload['assignees']]
        return copy.deepcopy(item)


def fixture_plan():
    person = {'track': 'react-web', 'github': 'PratikTalware26'}
    plans = {(person['track'], person['github'], n): {
        'session': n, 'title': f'[Frontend react-web] PratikTalware26 | Session {n:03d}',
        'body': f'Implement frontend increment {n}', 'labels': ['frontend-learning']}
        for n in range(1, 11)}
    return {'prepared_limit': 7, 'learners': [person]}, plans


class FrontendQueueRules(unittest.TestCase):
    def setUp(self):
        quiet = patch.object(queue, 'print', create=True)
        quiet.start()
        self.addCleanup(quiet.stop)

    def test_separate_initial_queue_is_idempotent_and_preserves_core(self):
        fake = FakeGitHub()
        original = copy.deepcopy(fake.issues[0])
        with patch.object(queue, 'gh', fake), patch.object(queue, 'read_plan', fixture_plan):
            queue.reconcile('owner/repo')
            queue.reconcile('owner/repo')
        self.assertEqual(fake.issues[0], original)
        frontend = fake.issues[1:]
        self.assertEqual(len(frontend), 7)
        self.assertEqual(sum(bool(i['assignees']) for i in frontend), 1)
        self.assertTrue(all(issue_key(i) is None for i in frontend))

    def test_closure_without_review_refills_but_does_not_assign_next(self):
        fake = FakeGitHub()
        with patch.object(queue, 'gh', fake), patch.object(queue, 'read_plan', fixture_plan):
            queue.reconcile('owner/repo')
            first = fake.issues[1]
            first.update(state='closed', state_reason='completed')
            queue.reconcile('owner/repo')
            active = [i for i in fake.issues[1:] if i['state'] == 'open']
            self.assertEqual(len(active), 7)
            self.assertFalse(any(i['assignees'] for i in active))
            first['labels'].append({'name': 'review-approved'})
            queue.reconcile('owner/repo')
            self.assertEqual([queue.task_key(i)[2] for i in active if i['assignees']], [2])

    def test_dry_run_has_no_mutations(self):
        fake = FakeGitHub()
        with patch.object(queue, 'gh', fake), patch.object(queue, 'read_plan', fixture_plan):
            queue.reconcile('owner/repo', dry_run=True)
        self.assertEqual(fake.mutations, [])

    def test_delayed_issue_listing_retries_reads_without_duplicate_creates(self):
        fake = FakeGitHub()
        omitted = []

        def delayed(*args, payload=None):
            result = fake(*args, payload=payload)
            if payload is None and 'state=open' in args[1] and not omitted:
                omitted.append(True)
                return [result[0][:-1]]
            return result

        with patch.object(queue, 'gh', delayed), patch.object(queue, 'read_plan', fixture_plan), patch.object(queue.time, 'sleep') as pause:
            queue.reconcile('owner/repo')
        self.assertEqual(len(fake.issues[1:]), 7)
        self.assertEqual(len(fake.mutations), 7)
        pause.assert_called_once_with(2)

    def test_persistent_verification_difference_fails_without_rewriting_work(self):
        fake = FakeGitHub()
        with patch.object(queue, 'gh', fake), patch.object(queue.time, 'sleep'):
            with self.assertRaisesRegex(RuntimeError, 'after read retries'):
                queue.verify_queues('owner/repo', [{'track':'react-web','github':'PratikTalware26','window':[1], 'current_session':1}])
        self.assertEqual(fake.mutations, [])

    def test_marker_cannot_adopt_python_or_unlabeled_issue(self):
        fake = FakeGitHub()
        item = fake.issues[0]
        self.assertIsNone(queue.task_key(item))
        item['body'] = '<!-- frontend-task: react-web/PratikTalware26/001 -->'
        with self.assertRaises(ValueError):
            queue.task_key(item)
        item['title'] = '[Frontend react-web] pretend'
        with self.assertRaises(ValueError):
            queue.task_key(item)

    def test_no_moving_extra_frontend_issues(self):
        fake = FakeGitHub()
        with patch.object(queue, 'gh', fake), patch.object(queue, 'read_plan', fixture_plan):
            queue.reconcile('owner/repo')
            extra = copy.deepcopy(fake.issues[-1])
            extra['number'] = 999
            extra['body'] = extra['body'].replace('/007 -->', '/010 -->')
            fake.issues.append(extra)
            before = copy.deepcopy(fake.issues)
            with self.assertRaises(ValueError):
                queue.reconcile('owner/repo')
            self.assertEqual(fake.issues, before)

    def test_real_plans_are_separate_complete_and_backend_bound(self):
        config, plans = queue.read_plan()
        self.assertEqual(len(plans), 90)
        expected = {'PratikTalware26': ('react-web', 28), 'praadeep28101995': ('react-web', 28), 'bitsnbyt3s': ('react-native', 34)}
        files = {}
        for person in config['learners']:
            track, count = expected[person['github']]
            self.assertEqual((person['track'], person['planned_sessions']), (track, count))
            rows = [p for (t, g, n), p in plans.items() if g == person['github']]
            self.assertEqual(rows[0]['lesson'], 'J01')
            for row in rows:
                self.assertIn('Python', row['body'])
                self.assertIn('review', row['body'])
                for filename in row['files']:
                    if filename in files:
                        self.assertEqual(files[filename], person['github'])
                    files[filename] = person['github']
            if track == 'react-native':
                self.assertEqual([p['lesson'] for p in rows][14:20], [f'R{i:02d}' for i in range(1, 7)])
                self.assertTrue(all(p.startswith('clients/learning/') for row in rows[14:20] for p in row['files']))


if __name__ == '__main__':
    unittest.main()
