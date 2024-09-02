import requests

def simple_get():
    url = 'https://reqbin.com/echo'
    response = requests.get(url, timeout=5)
    return response
