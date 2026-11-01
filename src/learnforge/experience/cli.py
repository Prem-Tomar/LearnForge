"""Initial working command; later behavior is learner implementation work."""
from learnforge.adapters.console import format_status
from learnforge.core.project import project_status


def main():
    print(format_status(project_status()))
