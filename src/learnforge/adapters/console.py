"""Simple output formatting; no external dependencies."""


def format_status(status):
    return "\n".join(
        [
            status["name"],
            "Stage: " + status["stage"],
            "Implemented: " + status["implemented"],
            "Next: " + status["next"],
        ]
    )
