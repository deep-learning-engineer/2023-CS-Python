from calculator import calculate, prefix_evaluate, to_prefix


def test_prefix_evaluate():
    assert prefix_evaluate("+ 2 3") == 5, "Must be 5"
    assert prefix_evaluate("+ - 2 3 5") == 4, "Must be 4"


def test_to_prefix():
    assert to_prefix("1 + ( 2 - 3 ) * 2") == ["+", "1", "*", "-", "2", "3", "2"]


def test_calculate():
    assert calculate("1 + ( 2 - 3 ) * 2") == eval("1 + ( 2 - 3 ) * 2")
