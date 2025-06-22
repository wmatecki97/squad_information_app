from app.settings import settings
from app.models import PlayerDetail
from app.services.football_api_client import FootballAPIClient
from typing import Optional
from datetime import datetime


class PlayerDetailFetcher:
    """
    Component 3: Fetches detailed profile information for players.
    """
    def __init__(self, api_client: FootballAPIClient):
        self.api_client = api_client

    def get_details_for_player(self, player_id: int) -> Optional[PlayerDetail]:
        """Fetches detailed profile for a single player by their ID."""
        current_season = datetime.now().year

        if settings.is_trial_football_api_key:
            current_season = datetime.now().year - 3

        response_data = self.api_client.make_request(
            "players",
            params={"id": str(player_id), "season": str(current_season)}
        )
        if not response_data:
            return None

        try:
            player_full_data = response_data[0]
            return PlayerDetail(**player_full_data['player'])
        except (IndexError, KeyError, Exception) as e:
            print(f"Error parsing player detail for ID {player_id}: {e}")
            return None
        