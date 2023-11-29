import lasku


def test_add():
    result = lasku.add(5, 4)
    assert result, 9


def test_multiply():
    result = lasku.multiply(3, 4)
    assert result, 12

def test_power():
    result = lasku.power(2, 8)
    assert result, 256
