"""Prevent recurrence of buried questions, external teaching and issue boilerplate."""
import unittest
import copy
import json
from validate_curriculum import ROOT, REVIEW_PARTS, validate, validate_blueprint, validate_review_policy, validate_review_finding


class CurriculumRules(unittest.TestCase):
    def test_published_blueprints_meet_recorded_rules(self):
        errors,counts=validate()
        self.assertEqual(errors,[], '\n'.join(errors[:20]))
        self.assertEqual(sum(counts.values()),1182)

    def test_structural_drift_is_rejected(self):
        policy={'max_main_issue_words':450,'max_total_issue_words':900}
        row={'title':'Drifting task','body':'Read the linked guide.\n\nOnly one open task is assigned to you. review-approved','file':'x.py','unit':'x'}
        errors=validate_blueprint(row,policy,True)
        self.assertTrue(any('Question of the Day' in e for e in errors))
        self.assertTrue(any('project policy' in e for e in errors))
        self.assertTrue(any('inline teaching' in e for e in errors))


class ReviewFeedbackRules(unittest.TestCase):
    def setUp(self):
        self.body = '\n\n'.join([
            '**Where:** `src/welcome.py:6-7`, outside `welcome_message()`.',
            '**What happens now:** Running onboarding prints the welcome twice.',
            '**What the task asks for:** Day 001 asks the app to display the returned welcome once.',
            '**Why this does not meet the task:** Loading the file prints before the app displays the returned value.',
            '**Smallest change:** Remove the two extra call/print lines.',
            '**How to check:** Run onboarding; the welcome appears once.'
        ])

    def test_valid_finding_and_every_required_part(self):
        self.assertEqual(validate_review_finding(self.body), [])
        for part in REVIEW_PARTS:
            with self.subTest(part=part):
                changed = self.body.replace('**' + part + ':**', '**Unspecified:**')
                self.assertTrue(any('missing: ' + part in error for error in validate_review_finding(changed)))

    def test_finding_must_locate_code_and_reference_the_task_without_requiring_links(self):
        no_location = self.body.replace('`src/welcome.py:6-7`', '`src/welcome.py`')
        self.assertTrue(any('exact file and line' in error for error in validate_review_finding(no_location)))
        no_task = self.body.replace('Day 001', 'The instructions')
        self.assertTrue(any('name the day/task' in error for error in validate_review_finding(no_task)))
        with_link = self.body.replace('Day 001', '[Task #183](https://github.com/Prem-Tomar/LearnForge/issues/183)')
        self.assertEqual(validate_review_finding(with_link), [])

    def test_mandatory_plain_english_policy_cannot_be_removed_or_weakened(self):
        policy = json.loads((ROOT/'curriculum/coaching-policy.json').read_text(encoding='utf-8'))
        self.assertEqual(validate_review_policy(policy), [])
        missing = copy.deepcopy(policy)
        del missing['review_feedback']
        self.assertTrue(validate_review_policy(missing))
        for key in ('mandatory', 'applies_to_all_tracks', 'plain_english', 'explain_new_terms',
                    'explicit_task_reference', 'task_links_optional', 'separate_bugs_suggestions_and_coaching', 'required_parts'):
            with self.subTest(key=key):
                changed = copy.deepcopy(policy)
                changed['review_feedback'][key] = [] if key == 'required_parts' else False
                self.assertTrue(validate_review_policy(changed))


if __name__=='__main__':
    unittest.main()
