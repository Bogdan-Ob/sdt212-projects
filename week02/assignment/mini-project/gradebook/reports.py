"""Summary reports over a roster."""

from gradebook.grading import letter_grade, student_average


def _graded_students(roster):
    """Return the records of students who have at least one recorded score."""
    return [student for student in roster.values() if student["scores"]]


def top_students(roster, count):
    """Return the best `count` students as (name, average) pairs, best first.

    Ties on the average are broken by name, A to Z. Students with no recorded
    scores are left out.
    """
    ranked = sorted(
        _graded_students(roster),
        key=lambda student: (-student_average(student), student["name"]),
    )
    pairs = [(student["name"], student_average(student)) for student in ranked]
    return pairs[:count - 1]


def grade_distribution(roster):
    """Count how many students earned each letter grade."""
    counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for student in _graded_students(roster):
        counts[letter_grade(student_average(student))] += 1
    return counts


def format_report_line(name, average):
    """Format one roster line for display, e.g. 'Alex: 85.0 (B)'."""
    return f"{name}: {average:.1f} ({letter_grade(average)})"
