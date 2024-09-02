from python_skeleton.squarer.squarer import square

def test_square():
    # Given
    number=4

    # When
    subject = square(number)

    # Then
    assert subject == 16
