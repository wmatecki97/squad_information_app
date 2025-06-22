import requests


class FootballAPIClient:
    """Helper class to manage all interactions with the football API."""
    def __init__(self, api_key: str, api_host: str):
        self.base_url = f"https://{api_host}"
        self.headers = {
            "x-rapidapi-key": api_key,
            "x-rapidapi-host": api_host
        }

    def make_request(self, endpoint: str, params: dict):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            if not data.get("response") or data.get("results") == 0:
                print(f"API returned no results for {endpoint} with params {params}. Errors: {data.get('errors')}")
                return None
            return data["response"]
        except requests.exceptions.RequestException as e:
            print(f"HTTP Request failed: {e}")
            return None