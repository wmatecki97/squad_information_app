import pytest
from app.services.query_router import QueryRouter

@pytest.mark.parametrize("query_str", [
    "When is the next Arsenal match?",
    "What was the score in the last Liverpool game?",
    "Who is the top scorer for Chelsea?",
    "Tottenham Hotspur recent results",
    "West Ham's manager history",
    "Where is Brighton in the league table?",
    "Newcastle United transfer news",
    "Aston Villa home stadium?",
    "Crystal Palace fixture list",
    "Wolves injury update",
    "Burnley vs Leeds predictions",
    "Everton match highlights",
    "Brentford match postponed?",
    "Fulham's points this season",
    "Sheffield United goals conceded",
    "Manchester United vs City result",
    "History of Leicester City FC",
    "Who owns Bournemouth?",
    "Luton Town's coach name",
    "Watford fan chants",
    "Best Fulham players of all time",
    "Chelsea stadium capacity",
    "Arsenal's best XI this season",
    "Liverpool upcoming schedule",
    "Brighton average attendance",
    "Manchester City net spend",
    "Newcastle trophy wins",
    "Wolves vs Aston Villa rivalry",
    "West Ham fanbase size",
    "Tottenham kit colors",
])
def test_query_router_out_of_scope_premier_league(query_router: QueryRouter, query_str: str):
    result = query_router.analyze(query_str, history_str="")
    assert result.is_squad_query is False
    assert result.team_name is None
    assert result.simple_team_name is None
