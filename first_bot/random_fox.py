import requests
from urllib3 import request


def random_fox():
    url = 'https://randomfox.ca/floof/'
    response = requests.get(url)
    if response.status_code:
        data = response.json()
        return data.get('image')

if __name__ == "__main__":
    random_fox()