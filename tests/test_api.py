from python_skeleton.api.request import simple_get

def test_simple_get():
    # When
    response = simple_get()

    # Then
    assert response.response_code == 200
