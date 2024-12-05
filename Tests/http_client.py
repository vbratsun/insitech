import requests

class HttpClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None, headers=None):
        response = requests.get(f"{self.base_url}{endpoint}", params=params, headers=headers)
        self._check_response(response)
        return response

    def post(self, endpoint, data=None, json=None, headers=None):
        response = requests.post(f"{self.base_url}{endpoint}", data=data, json=json, headers=headers)
        self._check_response(response)
        return response

    def put(self, endpoint, data=None, json=None, headers=None):
        response = requests.put(f"{self.base_url}{endpoint}", data=data, json=json, headers=headers)
        self._check_response(response)
        return response

    def delete(self, endpoint, headers=None):
        response = requests.delete(f"{self.base_url}{endpoint}", headers=headers)
        self._check_response(response)
        return response

    def _check_response(self, response):
        if not response.ok:
            raise Exception(f"HTTP {response.status_code}: {response.text}")