import jwt
import uuid
import hashlib
from urllib.parse import urlencode
import requests
from config.settings import UPBIT_ACCESS_KEY, UPBIT_SECRET_KEY, UPBIT_SERVER_URL

class UpbitAuth:
    def __init__(self):
        self.access_key = UPBIT_ACCESS_KEY
        self.secret_key = UPBIT_SECRET_KEY
        self.server_url = UPBIT_SERVER_URL

    def _create_token(self, query=None):
        payload = {
            'access_key': self.access_key,
            'nonce': str(uuid.uuid4()),
        }

        if query is not None:
            query_string = urlencode(query)
            payload['query'] = query_string

        jwt_token = jwt.encode(payload, self.secret_key)
        return jwt_token

    def get_headers(self, query=None):
        token = self._create_token(query)
        return {"Authorization": f"Bearer {token}"}

    def request_get(self, endpoint, params=None):
        url = f"{self.server_url}{endpoint}"
        headers = self.get_headers(params)
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def request_post(self, endpoint, data=None):
        url = f"{self.server_url}{endpoint}"
        headers = self.get_headers()
        response = requests.post(url, headers=headers, json=data)
        return response.json()