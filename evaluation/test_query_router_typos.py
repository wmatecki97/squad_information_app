import pytest
from app.services.query_router import QueryRouter

@pytest.mark.parametrize("query_str, expected_team", [ 
    ("Who is in the Mancester City team?", "Manchester City"),
    ("Arsnl players list", "Arsenal"),
    ("Chelseaa full squad?", "Chelsea"),
    ("Tottenhm Hotspur team?", "Tottenham Hotspur"),
    ("Livrpool FD current players", "Liverpool FC"),
    ("Westham United line-up", "West Ham United"),
    ("Brightin squad please", "Brighton & Hove Albion"),
    ("Newcaste United squad", "Newcastle United"),
    ("Everon full list", "Everton"),
    ("Fuhlam FC players", "Fulham FC"),
    ("Crysatl Palace squad", "Crystal Palace"),
    ("Wolves current lineup", "Wolverhampton Wanderers"),
    ("AFC Bornmouth full squad", "AFC Bournemouth"),
    ("Leeds Unitted players", "Leeds United"),
    ("Southamton FC squad", "Southampton FC"),
    ("Nottinghm Forest team", "Nottingham Forest"),
    ("Brentfordd FC players", "Brentford FC"),
    ("Sheffeild United list", "Sheffield United"),
    ("Lutn Town squad", "Luton Town"),
])
def test_query_router_typos(query_router: QueryRouter, query_str: str, expected_team: str):
    result = query_router.analyze(query_str, history_str="")
    assert result.is_squad_query is True
    assert result.team_name == expected_team
    assert result.refer_to_current_squad is True