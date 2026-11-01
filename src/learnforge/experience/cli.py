"""Initial working command; later behavior is learner implementation work."""
import sys

from learnforge.experience.commands.onboarding import show_onboarding
from learnforge.experience.commands.welcome import show_status
from learnforge.experience.workflows.welcome import welcome_status


def main():
    if sys.argv[1:] == ["onboarding"]:
        show_onboarding()
    else:
        show_status(welcome_status())
