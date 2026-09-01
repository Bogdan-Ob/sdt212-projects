from gradebook import reports, students


def build_roster():
    """Dana 98.0 (A), Alex 80.0 (B), Bo 72.0 (C), Casey 58.0 (F)."""
    roster = students.new_roster()
    for student_id, name, scores in (
        ("s1", "Alex", (80, 80)),
        ("s2", "Bo", (70, 74)),
        ("s3", "Casey", (55, 61)),
        ("s4", "Dana", (99, 97)),
    ):
        students.add_student(roster, student_id, name)
        for score in scores:
            students.record_score(roster, student_id, score)
    return roster


def test_top_students_returns_the_requested_number_in_rank_order():
    roster = build_roster()
    top = reports.top_students(roster, 3)
    assert [name for name, _ in top] == ["Dana", "Alex", "Bo"]
    assert top[0] == ("Dana", 98.0)


def test_top_students_returns_everyone_when_count_exceeds_the_roster():
    roster = build_roster()
    top = reports.top_students(roster, 10)
    assert [name for name, _ in top] == ["Dana", "Alex", "Bo", "Casey"]


def test_grade_distribution_counts_each_letter():
    roster = build_roster()
    assert reports.grade_distribution(roster) == {
        "A": 1,
        "B": 1,
        "C": 1,
        "D": 0,
        "F": 1,
    }


def test_grade_distribution_of_an_empty_roster_is_all_zeroes():
    assert reports.grade_distribution(students.new_roster()) == {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0,
    }


def test_format_report_line_shows_the_average_and_letter():
    assert reports.format_report_line("Alex", 80.0) == "Alex: 80.0 (B)"
    assert reports.format_report_line("Casey", 58.0) == "Casey: 58.0 (F)"
