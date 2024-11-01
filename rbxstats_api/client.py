import requests

class RbxStatsClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.rbxstats.xyz/api"
        
        # Initialize endpoint classes
        self.offsets = Offsets(self.api_key, self.base_url)
        self.exploits = Exploits(self.api_key, self.base_url)
        self.versions = Versions(self.api_key, self.base_url)
        self.games = Games(self.api_key, self.base_url)

class BaseEndpoint:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def _make_request(self, endpoint):
        """Internal method to make GET requests to the specified endpoint."""
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
        return response.json()

# Offsets endpoints
class Offsets(BaseEndpoint):
    def get_all_offsets(self, plain_text=False):
        """Fetch all Roblox offsets."""
        url = f"{self.base_url}/offsets"
        if plain_text:
            url += "/plain"
        return self._make_request(f"{url}?api={self.api_key}")

    def get_offset_by_name(self, name, plain_text=False):
        """Fetch a specific Roblox offset by name."""
        url = f"{self.base_url}/offsets/search/{name}"
        if plain_text:
            url += "/plain"
        return self._make_request(f"{url}?api={self.api_key}")

    def get_offsets_by_prefix(self, prefix, plain_text=False):
        """Fetch offsets with a specific prefix."""
        url = f"{self.base_url}/offsets/prefix/{prefix}"
        if plain_text:
            url += "/plain"
        return self._make_request(f"{url}?api={self.api_key}")

    def get_camera_offsets(self, plain_text=False):
        """Fetch all camera-related offsets."""
        url = f"{self.base_url}/offsets/camera"
        if plain_text:
            url += "/plain"
        return self._make_request(f"{url}?api={self.api_key}")

# Exploits endpoints
class Exploits(BaseEndpoint):
    def get_all_exploits(self):
        """Fetch all current working exploits."""
        return self._make_request(f"{self.base_url}/exploits?api={self.api_key}")

    def get_windows_exploits(self):
        """Fetch all current working Windows exploits."""
        return self._make_request(f"{self.base_url}/windows?api={self.api_key}")

    def get_mac_exploits(self):
        """Fetch all current working Mac exploits."""
        return self._make_request(f"{self.base_url}/mac?api={self.api_key}")

    def get_detected_exploits(self):
        """Fetch all currently detected exploits."""
        return self._make_request(f"{self.base_url}/detected?api={self.api_key}")

    def get_undetected_exploits(self):
        """Fetch all currently undetected exploits."""
        return self._make_request(f"{self.base_url}/undetected?api={self.api_key}")

    def get_free_exploits(self):
        """Fetch all currently free exploits."""
        return self._make_request(f"{self.base_url}/free?api={self.api_key}")

    def get_paid_exploits(self):
        """Fetch all currently paid exploits."""
        return self._make_request(f"{self.base_url}/paid?api={self.api_key}")

    def get_in_development_exploits(self):
        """Fetch all exploits in development."""
        return self._make_request(f"{self.base_url}/indev?api={self.api_key}")

    def get_exploit_summary(self):
        """Get a summary of detected and undetected exploits."""
        return self._make_request(f"{self.base_url}/summary?api={self.api_key}")

    def get_exploit_count(self):
        """Get the total number of exploits."""
        return self._make_request(f"{self.base_url}/count?api={self.api_key}")

# Versions endpoints
class Versions(BaseEndpoint):
    def get_latest_version(self):
        """Fetch the latest Roblox version."""
        return self._make_request(f"{self.base_url}/versions/latest?api={self.api_key}")

    def get_future_version(self):
        """Fetch the future Roblox version."""
        return self._make_request(f"{self.base_url}/versions/future?api={self.api_key}")

# Games endpoints
class Games(BaseEndpoint):
    def get_game_info(self, game_id, plain_text=False):
        """Fetch game information for a specific game ID."""
        url = f"{self.base_url}/offsets/game/{game_id}"
        if plain_text:
            url += "/plain"
        return self._make_request(f"{url}?api={self.api_key}")
