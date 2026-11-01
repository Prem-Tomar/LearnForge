"""Prevent recurrence of buried questions, external teaching and issue boilerplate."""
import unittest
from validate_curriculum import validate, validate_blueprint


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


if __name__=='__main__':
    unittest.main()
