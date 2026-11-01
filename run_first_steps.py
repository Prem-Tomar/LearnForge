"""Provided runner: learners edit their own tiny onboarding function first."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from learnforge.experience.onboarding.learner_01 import project_title
from learnforge.experience.onboarding.learner_02 import welcome_message
from learnforge.experience.onboarding.learner_03 import today_topic
from learnforge.experience.onboarding.learner_04 import planned_minutes
from learnforge.experience.onboarding.learner_05 import next_step
from learnforge.experience.onboarding.learner_06 import ready_message


def main():
    print("LearnForge first steps")
    print("Project:", project_title())
    print(welcome_message())
    print("Topic:", today_topic())
    print("Study minutes:", planned_minutes())
    print("Next:", next_step())
    print("Status:", ready_message())


if __name__ == "__main__":
    main()
