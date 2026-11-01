"""Small maintainer checks for queue correctness, not learner assignments."""
import unittest
from learning_queue import desired_window, is_completed


def issue(state="open", reason=None, deferred=False):
    return {"state": state, "state_reason": reason, "labels": [{"name": "queue-deferred"}] if deferred else []}


class QueueRules(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
