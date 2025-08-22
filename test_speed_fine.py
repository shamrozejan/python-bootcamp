#test_speed_fine.py

from fines import speed_fine

def test_ok_exact():
    assert speed_fine(40,40) == "OK"

def test_small_over():
    assert speed_fine(45,40) == "$50"

def test_edge_10():
    assert speed_fine(50,40) == "$50"

def test_edge_20():
    assert speed_fine(60,40) == "$150"

def test_over_20():
    assert speed_fine(61,40) == "$300"
