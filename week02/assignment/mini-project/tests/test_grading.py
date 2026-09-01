from gradebook import grading, students


def build_roster():
    """Alex averages 85.0, Bo averages 95.0."""
    roster = students.new_roster()
    students.add_student(roster, "s1", "Alex")
    students.add_student(roster, "s2", "Bo")
    for score in (80, 90):
        students.record_score(roster, "s1", score)
    for score in (95, 95):
        students.record_score(roster, "s2", score)
    return roster


def test_letter_grade_maps_scores_inside_each_band():
    assert grading.letter_grade(95) == "A"
    assert grading.letter_grade(85) == "B"
    assert grading.letter_grade(75) == "C"
    assert grading.letter_grade(65) == "D"
    assert grading.letter_grade(12) == "F"


def test_letter_grade_band_cutoffs_are_inclusive():
    assert grading.letter_grade(90) == "A"
    assert grading.letter_grade(80) == "B"
    assert grading.letter_grade(70) == "C"
    assert grading.letter_grade(60) == "D"
    assert grading.letter_grade(59) == "F"


def test_student_average_of_recorded_scores():
    roster = build_roster()
    assert grading.student_average(roster["s1"]) == 85.0
    assert grading.student_average(roster["s2"]) == 95.0


def test_student_average_rounds_to_two_decimals():
    roster = students.new_roster()
    students.add_student(roster, "s1", "Alex")
    for score in (70, 80, 85):
        students.record_score(roster, "s1", score)
    assert grading.student_average(roster["s1"]) == 78.33


def test_class_average_of_the_student_averages():
    roster = build_roster()
    assert grading.class_average(roster) == 90.0


def test_averages_handle_students_with_no_recorded_scores():
    roster = build_roster()
    students.add_student(roster, "s3", "Casey")  # added, never scored

    assert grading.student_average(roster["s3"]) is None
    # Casey has no scores, so Casey does not move the class average.
    assert grading.class_average(roster) == 90.0
    assert grading.class_average({"s3": roster["s3"]}) is None
    assert grading.class_average(students.new_roster()) is None
