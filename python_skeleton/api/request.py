import requests

def simple_get():
    url = 'https://jsonplaceholder.typicode.com/todos/1'
    response = requests.get(url, timeout=5)
    return response
