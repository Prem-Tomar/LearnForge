"""Check topic-relative dates, mixed review and independent checkpoint completion."""
from datetime import date
import unittest

from revision_schedule import due_topics


def topic(learner="one", topic_id="variables", taught="2026-11-01"):
    return {"learner": learner, "track": "python", "topic_id": topic_id, "topic": topic_id, "taught_on": taught}


class RevisionDates(unittest.TestCase):
    def test_first_day_is_teaching_day_not_one_day_later(self):
        due = due_topics([topic()], [], date(2026, 11, 1))
        self.assertEqual([(r["checkpoint_day"], r["due_on"]) for r in due], [(1, "2026-11-01")])

    def test_all_checkpoints_use_topic_relative_day_numbers(self):
        due = due_topics([topic()], [], date(2026, 11, 15))
        self.assertEqual({r["checkpoint_day"]: r["due_on"] for r in due}, {1:"2026-11-01",3:"2026-11-03",7:"2026-11-07",10:"2026-11-10",15:"2026-11-15"})

    def test_multiple_topics_and_learners_remain_independent(self):
        due = due_topics([topic(), topic("one", "functions", "2026-11-03"), topic("two", taught="2026-11-04")], [], date(2026, 11, 3))
        self.assertEqual({(r["topic_id"],r["checkpoint_day"]) for r in due}, {("variables",1),("variables",3),("functions",1)})
        self.assertEqual({r["learner"] for r in due}, {"one"})

    def test_one_pass_does_not_pass_other_checkpoints_or_partial_work(self):
        attempt = {"learner":"one","track":"python","topic_id":"variables","checkpoint_day":"1","attempted_on":"2026-11-01","status":"passed"}
        due = due_topics([topic()], [attempt], date(2026, 11, 3))
        self.assertEqual([r["checkpoint_day"] for r in due], [3])
        attempt["status"] = "partial"
        self.assertEqual(len(due_topics([topic()], [attempt], date(2026, 11, 3))), 2)

    def test_duplicate_introduction_cannot_reset_cycle(self):
        with self.assertRaises(ValueError):
            due_topics([topic(), topic(taught="2026-11-02")], [], date(2026,11,3))


if __name__ == "__main__":
    unittest.main()
