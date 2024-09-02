from python_skeleton.api.request import simple_get

def test_simple_get():
    # Given

    # When
    response = simple_get()

    # Then
    assert response.status_code == 200, f"Failed with response: {response.text}"
