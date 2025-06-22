import pytest
from app.services.query_router import QueryRouter

@pytest.mark.parametrize("query_str, expected_team", [
    ("Who is on the Manchester City team?", "Manchester City"),
    ("Show me the Arsenal squad", "Arsenal"),
    ("Liverpool FC players list", "Liverpool FC"),
    ("Who plays for Chelsea?", "Chelsea"),
    ("Tottenham Hotspur squad?", "Tottenham Hotspur"),
    ("Manchester United full squad", "Manchester United"),
    ("West Ham United team list", "West Ham United"),
    ("Brighton & Hove Albion players", "Brighton & Hove Albion"),
    ("Brentford FC team", "Brentford FC"),
    ("Newcastle United squad", "Newcastle United"),
    ("Aston Villa squad members", "Aston Villa"),
    ("Crystal Palace full squad", "Crystal Palace"),
    ("Wolverhampton Wanderers players list", "Wolverhampton Wanderers"),
    ("Burnley FC players", "Burnley FC"),
    ("Nottingham Forest roster", "Nottingham Forest"),
    ("Bournemouth team players", "AFC Bournemouth"),
    ("Everton full squad", "Everton"),
    ("Fulham FC team list", "Fulham FC"),
    ("Sheffield United squad", "Sheffield United"),
    ("Luton Town squad list", "Luton Town"),
    ("Leicester City players", "Leicester City"),
    ("Leeds United team", "Leeds United"),
    ("Southampton FC full squad", "Southampton FC"),
    ("Watford players", "Watford"),
    ("Norwich City squad", "Norwich City"),
    ("Swansea City lineup", "Swansea City"),
    ("Cardiff City players", "Cardiff City"),
    ("Blackburn Rovers team", "Blackburn Rovers"),
    ("Hull City full team", "Hull City"),
    ("Stoke City players", "Stoke City"),
])
def test_query_router_team_name_premier_league(query_router: QueryRouter, query_str: str, expected_team: str):
    result = query_router.analyze(query_str, history_str="")
    assert result.team_name == expected_team
