"""Small maintainer checks for queue correctness, not learner assignments."""
import unittest
from unittest.mock import patch
from learning_queue import desired_window, is_completed, eligible_current_day, compose_body, assigned_days, verify_queues


def issue(state="open", reason=None, deferred=False):
    return {"state": state, "state_reason": reason, "labels": [{"name": "queue-deferred"}] if deferred else []}


class QueueRules(unittest.TestCase):
    def test_assign_all_prepared_python_days_without_changing_current_gate(self):
        window=list(range(1,8))
        self.assertEqual(assigned_days(window,1,7,'learner'),window)
        self.assertEqual(assigned_days(window,None,7,'learner'),window)
        self.assertEqual(assigned_days(window,1,1,'learner'),[1])
        self.assertEqual(assigned_days(window,None,1,'learner'),[])
        self.assertEqual(assigned_days(window,1,7,None),[])

    def test_task_body_does_not_reintroduce_project_policy(self):
        rendered = compose_body({'learner':1, 'day':1, 'body':'## Goal\n\nImplement the small unit.'}, None, 'owner/repo')
        self.assertIn('Implement the small unit.', rendered)
        self.assertNotIn('review-approved', rendered)
        self.assertNotIn('Rolling queue', rendered)
        self.assertNotIn('Review, closure', rendered)

    def test_initial_window_is_seven(self):
        self.assertEqual(desired_window(range(1, 183), {}), list(range(1, 8)))

    def test_resolution_moves_to_next_day(self):
        current = {n: issue() for n in range(1, 8)}
        current[1] = issue("closed", "completed")
        self.assertEqual(desired_window(range(1, 183), current), list(range(2, 9)))

    def test_deferred_is_unfinished_and_reused(self):
        current = {n: issue("closed", "completed") for n in range(1, 8)}
        current[8] = issue("closed", "not_planned", True)
        self.assertEqual(desired_window(range(1, 183), current), list(range(8, 15)))
        self.assertFalse(is_completed(current[8]))

    def test_end_shrinks_without_inventing_work(self):
        current = {n: issue("closed", "completed") for n in range(1, 180)}
        self.assertEqual(desired_window(range(1, 183), current), [180, 181, 182])

    def test_finished_has_no_new_task(self):
        current = {n: issue("closed", "completed") for n in range(1, 183)}
        self.assertEqual(desired_window(range(1, 183), current), [])

    def test_out_of_order_close_does_not_skip_earlier_work(self):
        current = {5: issue("closed", "completed")}
        self.assertEqual(desired_window(range(1, 183), current), [1, 2, 3, 4, 6, 7, 8])

    def test_next_assignment_requires_review_and_closure(self):
        current = {1: issue("closed", "completed")}
        self.assertIsNone(eligible_current_day(range(1, 183), current, "learner"))
        current[1]["labels"] = [{"name": "review-approved"}]
        self.assertEqual(eligible_current_day(range(1, 183), current, "learner"), 2)
        current[1]["state"] = "open"
        self.assertEqual(eligible_current_day(range(1, 183), current, "learner"), 1)
        self.assertIsNone(eligible_current_day(range(1, 183), current, None))


class QueueReadVerification(unittest.TestCase):
    def setUp(self):
        self.plans = {(3, day): {} for day in range(2, 9)}
        self.summary = [{"learner": 3, "window": list(range(2, 9)), "assigned_days": list(range(2, 9)),
                         "github": "Rohan5607", "current_eligible_day": 2}]
        self.rows = [{"number": day, "title": f"Learner 03 | Day {day:03d}: Lesson", "assignees": [{"login": "Rohan5607"}],
                      "labels": [{"name": "queue-current"}] if day == 2 else []} for day in range(2, 9)]

    @patch("learning_queue.time.sleep")
    @patch("learning_queue.gh")
    def test_stale_list_then_fresh_list_uses_only_reads(self, gh, sleep):
        gh.side_effect = [[self.rows[:-1]], [self.rows]]
        verify_queues("owner/repo", self.summary, self.plans)
        self.assertEqual(gh.call_count, 2)
        sleep.assert_called_once_with(2)
        for call in gh.call_args_list:
            self.assertEqual(call.args, ("api", "repos/owner/repo/issues?state=open&per_page=100", "--paginate", "--slurp"))
            self.assertFalse(call.kwargs)

    @patch("learning_queue.time.sleep")
    @patch("learning_queue.gh")
    def test_persistent_missing_task_stops_after_four_reads(self, gh, sleep):
        gh.return_value = [self.rows[:-1]]
        with self.assertRaisesRegex(RuntimeError, "after read retries"):
            verify_queues("owner/repo", self.summary, self.plans)
        self.assertEqual(gh.call_count, 4)
        self.assertEqual(sleep.call_count, 3)

    @patch("learning_queue.time.sleep")
    @patch("learning_queue.gh")
    def test_wrong_assignee_or_current_step_cannot_pass(self, gh, sleep):
        for defect in ("assignee", "current"):
            with self.subTest(defect=defect):
                self.setUp()
                if defect == "assignee":
                    self.rows[-1]["assignees"] = [{"login": "other"}]
                else:
                    self.rows[-1]["labels"] = [{"name": "queue-current"}]
                gh.return_value = [self.rows]
                with self.assertRaises(RuntimeError):
                    verify_queues("owner/repo", self.summary, self.plans)


if __name__ == "__main__":
    unittest.main()
