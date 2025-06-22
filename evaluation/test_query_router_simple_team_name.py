import pytest
from app.services.query_router import QueryRouter

@pytest.mark.parametrize("query_str, expected_simple", [
    ("Show me the Arsenal squad", "Arsenal"),
    ("Liverpool FC players list", "Liverpool"),
    ("Chelsea full squad", "Chelsea"),
    ("Tottenham Hotspur team", "Tottenham"),
    ("Brighton & Hove Albion players", "Brighton"),
    ("Brentford FC team", "Brentford"),
    ("Newcastle United squad", "Newcastle"),
    ("Wolverhampton Wanderers players", "Wolves"),
    ("Burnley FC squad", "Burnley"),
    ("Bournemouth players", "Bournemouth"),
    ("Everton player list", "Everton"),
    ("Fulham FC players", "Fulham"),
    ("Luton Town players", "Luton"),
    ("Leicester City squad", "Leicester"),
    ("Leeds United lineup", "Leeds"),
    ("Southampton FC squad", "Southampton"),
    ("Watford team list", "Watford"),
    ("Norwich City players", "Norwich"),
    ("Swansea City full squad", "Swansea"),
    ("Cardiff City team", "Cardiff"),
    ("Blackburn Rovers squad", "Blackburn"),
    ("Derby County players", "Derby"),
])
def test_query_router_simple_team_name_premier_league(query_router: QueryRouter, query_str: str, expected_simple: str):
    result = query_router.analyze(query_str, history_str="")
    assert result.simple_team_name == expected_simple
