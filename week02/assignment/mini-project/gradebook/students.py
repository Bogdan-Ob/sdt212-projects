"""Roster storage and input validation.

A roster is a dict mapping a student id to a record:

    {"s1": {"name": "Alex", "scores": [88, 92]}}
"""

MIN_SCORE = 0
MAX_SCORE = 100


def new_roster():
    """Return an empty roster."""
    return {}


def add_student(roster, student_id, name):
    """Add a student to the roster and return the new record.

    Raises ValueError if the id is already taken or the name is not usable.
    """
    if student_id in roster:
        raise ValueError(f"student id already in use: {student_id}")
    if not name:
        raise ValueError("student name must not be empty")
    roster[student_id] = {"name": name, "scores": []}
    return roster[student_id]


def record_score(roster, student_id, score):
    """Record one score for a student and return that student's score list.

    Raises KeyError for an unknown id, ValueError for an out-of-range score.
    """
    student = get_student(roster, student_id)
    if score < MIN_SCORE or score > MAX_SCORE:
        raise ValueError(
            f"score must be between {MIN_SCORE} and {MAX_SCORE}: {score}"
        )
    student["scores"].append(score)
    return student["scores"]


def get_student(roster, student_id):
    """Return one student's record. Raises KeyError if the id is unknown."""
    if student_id not in roster:
        raise KeyError(f"unknown student id: {student_id}")
    return roster[student_id]
