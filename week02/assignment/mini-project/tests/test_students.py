import pytest

from gradebook import students


def build_roster():
    roster = students.new_roster()
    students.add_student(roster, "s1", "Alex")
    students.add_student(roster, "s2", "Bo")
    return roster


def test_add_student_stores_name_and_empty_score_list():
    roster = students.new_roster()
    students.add_student(roster, "s1", "Alex")
    assert roster["s1"] == {"name": "Alex", "scores": []}


def test_add_student_rejects_duplicate_id():
    roster = build_roster()
    with pytest.raises(ValueError):
        students.add_student(roster, "s1", "Casey")


def test_add_student_rejects_empty_name():
    roster = students.new_roster()
    with pytest.raises(ValueError):
        students.add_student(roster, "s1", "")


def test_add_student_rejects_whitespace_only_name():
    roster = students.new_roster()
    with pytest.raises(ValueError):
        students.add_student(roster, "s1", "   ")
    assert roster == {}


def test_record_score_appends_scores_in_order():
    roster = build_roster()
    students.record_score(roster, "s1", 88)
    students.record_score(roster, "s1", 92)
    assert roster["s1"]["scores"] == [88, 92]


def test_record_score_accepts_the_range_endpoints():
    roster = build_roster()
    students.record_score(roster, "s1", 0)
    students.record_score(roster, "s1", 100)
    assert roster["s1"]["scores"] == [0, 100]


def test_record_score_rejects_a_score_above_the_maximum():
    roster = build_roster()
    with pytest.raises(ValueError):
        students.record_score(roster, "s1", 101)


def test_record_score_rejects_a_negative_score():
    roster = build_roster()
    with pytest.raises(ValueError):
        students.record_score(roster, "s1", -1)


def test_record_score_rejects_an_unknown_student():
    roster = build_roster()
    with pytest.raises(KeyError):
        students.record_score(roster, "nobody", 80)


def test_get_student_returns_the_stored_record():
    roster = build_roster()
    assert students.get_student(roster, "s2") == {"name": "Bo", "scores": []}
