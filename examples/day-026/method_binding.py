"""Worked Day 026 example, after functions, exceptions and classes."""


class StudySession:
    kind = "study"

    def __init__(self, minutes):
        if not self.valid_minutes(minutes):
            raise ValueError("minutes must be a nonnegative integer")
        self.minutes = minutes

    def add_minutes(self, extra):
        if not self.valid_minutes(extra):
            raise ValueError("extra must be a nonnegative integer")
        self.minutes += extra
        return self.minutes

    @classmethod
    def from_minutes(cls, minutes):
        return cls(minutes)

    @staticmethod
    def valid_minutes(value):
        return isinstance(value, int) and not isinstance(value, bool) and value >= 0


class FocusedSession(StudySession):
    pass


if __name__ == "__main__":
    first = StudySession(30)
    second = StudySession(10)
    first.add_minutes(5)
    print(first.minutes, second.minutes)
    focused = FocusedSession.from_minutes(15)
    print(type(focused).__name__)
    print(StudySession.valid_minutes(0), first.valid_minutes(0))
