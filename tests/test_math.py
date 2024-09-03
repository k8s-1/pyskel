from pyskel.math.sum import add


def test_add_positive_numbers():
    # Given
    a = 2
    b = 3

    # When
    result = add(a, b)

    # Then
    assert result == 5


def test_add_negative_numbers():
    # Given
    a = -2
    b = -3

    # When
    result = add(a, b)

    # Then
    assert result == -5


def test_add_mixed_numbers():
    # Given
    a = -2
    b = 3

    # When
    result = add(a, b)

    # Then
    assert result == 1
