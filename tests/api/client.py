import requests


class ApiClient:
    def __init__(self, url):
        self.url = url

    def post(self, endpoint=None, **kwargs):
        url = f'{self.url}{endpoint}'
        resp = requests.post(url=url, **kwargs)
        return resp.status_code, resp.json()

    def get(self, endpoint):
        url = f'{self.url}{endpoint}'
        resp = requests.get(url=url)
        return resp.status_code, resp.json()

    def delete(self, endpoint):
        url = f'{self.url}{endpoint}'
        resp = requests.delete(url=url)
        return resp.status_code, resp.json()