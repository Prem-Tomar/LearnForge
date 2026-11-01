"""Connect the first small feature functions to the product's onboarding screen."""
from learnforge.experience.onboarding.project_title import project_title
from learnforge.experience.onboarding.welcome_message import welcome_message
from learnforge.experience.onboarding.current_topic import today_topic
from learnforge.experience.onboarding.study_plan import planned_minutes
from learnforge.experience.onboarding.next_lesson import next_step
from learnforge.experience.onboarding.readiness import ready_message


def show_onboarding():
    print("LearnForge first steps")
    print("Project:", project_title())
    print(welcome_message())
    print("Topic:", today_topic())
    print("Study minutes:", planned_minutes())
    print("Next:", next_step())
    print("Status:", ready_message())
