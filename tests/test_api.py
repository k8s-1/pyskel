from python_skeleton.api.request import simple_get

def test_simple_get():
    # Given
    url = 'https://jsonplaceholder.typicode.com/todos/3'

    # When
    response = simple_get(url)

    # Then
    assert response.status_code == 200, f"Failed with response: {response.text}"
