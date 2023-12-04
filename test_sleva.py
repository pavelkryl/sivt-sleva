from sleva import zlevni

# tento soubor neměňte

def test_basic() -> None:
    assert zlevni(45,20) == 36

def test_default_value() -> None:
    assert zlevni(100) == 90

def test_no_sale() -> None:
    assert zlevni(1490.50, 0) == 1490.50