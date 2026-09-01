"""Score averages and letter grades."""

# Lowest numeric average that still earns each letter. Anything below the
# last cutoff is an F.
GRADE_BANDS = ((90, "A"), (80, "B"), (70, "C"), (60, "D"))


def letter_grade(average):
    """Return the letter grade for a numeric average."""
    for cutoff, letter in GRADE_BANDS:
        if average >= cutoff:
            return letter
    return "F"


def student_average(student):
    """Return one student's average score, rounded to two decimals."""
    scores = student["scores"]
    return round(sum(scores) / len(scores), 2)


def class_average(roster):
    """Return the average of the students' averages, rounded to two decimals."""
    averages = [student_average(student) for student in roster.values()]
    return round(sum(averages) / len(averages), 2)
