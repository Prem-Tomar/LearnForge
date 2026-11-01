"""Initial working command; later behavior is learner implementation work."""
from learnforge.experience.commands.welcome import show_status
from learnforge.experience.workflows.welcome import welcome_status


def main():
    show_status(welcome_status())
