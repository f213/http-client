from urllib.parse import urljoin

import httpx



class HTTPException(Exception):
    pass


class RateLimited(HTTPException):
    pass


class HTTP:
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    def __init__(self, token: str, host: str = 'https://host.io/api/', timeout: int = 6):
        self.host = host
        self.token = token
        self.timeout = timeout

    def _request(self, method: str, url: str, json: dict = None) -> dict:
        url = url.strip('/')
        url = urljoin(self.host, url)

        params = {
            'method': method,
            'url': url,
            'headers': {
                **self.headers,
                'X-auth-TOKEN': self.token,
            },
            'timeout': self.timeout,
        }

        if json:
            params['json'] = json

        response = httpx.request(**params)

        if response.status_code != 200:
            raise HTTPException(f'Non-200 response when fetching url {url}: {response.status_code}')

        return response.json()

    def get(self, url: str):
        return self._request('get', url)
