from Codewars.Maximize_Points.maximize_points import maximize_points

def test_small_team():
    assert maximize_points([3, 2, 4], [1, 2, 3]) == 3

def test_one_person_team():
    assert maximize_points([99], [1]) == 1

def test_large_team():
    assert maximize_points([7, 19, 23, 18, 38, 37, 38, 40], [21, 12, 1, 0, 13, 38, 25, 49]) == 7