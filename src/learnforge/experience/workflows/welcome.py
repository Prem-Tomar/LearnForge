from learnforge.adapters.storage.memory import starter_state
from learnforge.core.operations.status import build_status
from learnforge.core.values.project import PROJECT_NAME


def welcome_status():
    return build_status(PROJECT_NAME, **starter_state())
