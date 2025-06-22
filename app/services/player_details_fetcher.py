import logging
from app.settings import settings
from app.models import PlayerDetail
from app.services.football_api_client import FootballAPIClient
from typing import Optional
from datetime import datetime

logger = logging.getLogger(__name__)

class PlayerDetailFetcher:
    """
    Component 3: Fetches detailed profile information for players.
    """
    def __init__(self, api_client: FootballAPIClient):
        self.api_client = api_client

    def get_details_for_player(self, player_id: int) -> Optional[PlayerDetail]:
        """Fetches detailed profile for a single player by their ID."""

        response_data = self.api_client.make_request(
            "players/profiles",
            params={"player": str(player_id)}
        )
        if not response_data:
            return None

        try:
            player_full_data = response_data[0]
            return PlayerDetail(**player_full_data['player'])
        except (IndexError, KeyError, Exception) as e:
            logger.error(f"Error parsing player detail for ID {player_id}: {e}")
            return None
        