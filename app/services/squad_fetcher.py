from typing import List, Optional

from app.models import PlayerInSquad, TeamSearchResponse
from app.services.football_api_client import FootballAPIClient


class SquadFetcher:
    """
    Component 2: Fetches squad information (list of players) for a given team name.
    """
    def __init__(self, api_client: FootballAPIClient):
        self.api_client = api_client

    def _get_team_id(self, team_name: str) -> Optional[int]:
        """Finds the team ID from a team name using the /teams endpoint."""
        response_data = self.api_client.make_request("teams", params={"search": team_name})
        if not response_data:
            return None

        try:
            teams = [TeamSearchResponse(**item) for item in response_data]


            # Prioritize exact match, case-insensitive
            for team_info in teams:
                if team_info.team.name.lower() == team_name.lower():
                    return team_info.team.id

            # Fallback to the first result if no exact match
            #todo llm selection and asking user for clarification if required (not needed for PoC)
            if teams:
                return teams[0].team.id
        except Exception as e:
            print(f"Error parsing team data: {e}")

        return None

    def get_squad_player_info(self, team_name: str) -> Optional[List[PlayerInSquad]]:
        """Gets the list of players (ID, name, position) for a team."""
        team_id = self._get_team_id(team_name)
        if not team_id:
            print(f"Team '{team_name}' not found.")
            return None

        response_data = self.api_client.make_request("players/squads", params={"team": str(team_id)})
        if not response_data:
            return None

        try:
            squad_data = response_data[0] # Response is a list with one squad object
            return [PlayerInSquad(**p) for p in squad_data["players"]]
        except (IndexError, KeyError, Exception) as e:
            print(f"Error parsing squad data: {e}")
            return None