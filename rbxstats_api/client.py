import requests
from requests.exceptions import HTTPError, Timeout, RequestException

class RbxStatsClient:
    def __init__(self, api_key, base_url="https://api.rbxstats.xyz/api", timeout=5):
        self.api_key = api_key
        self.base_url = base_url
        self.timeout = timeout
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def _get(self, endpoint, params=None):
        if params is None:
            params = {}
        # Add the API key as a query parameter
        params["api"] = self.api_key
    
        try:
            response = requests.get(
                f"{self.base_url}/{endpoint}",
                headers=self.headers,
                params=params,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return {"error": str(http_err)}
        except Timeout:
            print("Request timed out.")
            return {"error": "Request timed out."}
        except RequestException as req_err:
            print(f"Network error: {req_err}")
            return {"error": str(req_err)}
        except ValueError as json_err:
            print(f"JSON decoding error: {json_err}")
            return {"error": "Error decoding JSON response."}

    def set_headers(self, additional_headers):
        """Set additional headers for the requests."""
        self.headers.update(additional_headers)

    def set_timeout(self, timeout):
        """Set custom timeout for requests."""
        self.timeout = timeout

    # Offsets nested class
    class Offsets:
        def __init__(self, client):
            self.client = client

        def all(self):
            return self.client._get("offsets")

        def by_name(self, name):
            return self.client._get(f"offsets/{name}")

        def by_prefix(self, prefix):
            return self.client._get(f"offsets/prefix/{prefix}")

        def camera(self):
            return self.client._get("offsets/camera")

    # Exploits nested class
    class Exploits:
        def __init__(self, client):
            self.client = client

        def all(self):
            return self.client._get("exploits")

        def windows(self):
            return self.client._get("exploits/windows")

        def mac(self):
            return self.client._get("exploits/mac")

        def undetected(self):
            return self.client._get("exploits/undetected")

        def detected(self):
            return self.client._get("exploits/detected")

        def free(self):
            return self.client._get("exploits/free")

    # Versions nested class
    class Versions:
        def __init__(self, client):
            self.client = client

        def latest(self):
            return self.client._get("versions/latest")

        def future(self):
            return self.client._get("versions/future")

    # Game nested class
    class Game:
        def __init__(self, client):
            self.client = client

        def by_id(self, game_id):
            return self.client._get(f"game/{game_id}")

    # Instance methods to access the nested classes
    def offsets(self):
        return self.Offsets(self)

    def exploits(self):
        return self.Exploits(self)

    def versions(self):
        return self.Versions(self)

    def game(self):
        return self.Game(self)
