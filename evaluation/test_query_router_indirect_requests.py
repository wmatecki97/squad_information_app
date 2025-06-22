import pytest
from app.services.query_router import QueryRouter

@pytest.mark.parametrize("query_str, expected_team", [
    ("Can you remind me who's playing for Chelsea?", "Chelsea"),
    ("Who's currently in the Liverpool FC dressing room?", "Liverpool FC"),
    ("What names come to mind when you think of Arsenal's current team?", "Arsenal"),
    ("Tell me who lines up for Spurs these days.", "Tottenham Hotspur"),
    ("What does the West Ham squad look like right now?", "West Ham United"),
    ("Could you name the Newcastle United players active this season?", "Newcastle United"),
    ("Who are Aston Villa's key squad members today?", "Aston Villa"),
    ("Let me know who’s currently part of Fulham FC.", "Fulham FC"),
    ("Who wears the jersey for Brentford FC nowadays?", "Brentford FC"),
    ("What kind of lineup does Crystal Palace have this season?", "Crystal Palace"),
    ("Point out Wolves players for this campaign.", "Wolverhampton Wanderers"),
    ("Give me the names making up AFC Bournemouth's side this year.", "AFC Bournemouth"),
    ("Leeds United current personnel?", "Leeds United"),
    ("Who’s currently in charge on the field for Southampton?", "Southampton FC"),
    ("Tell me who represents Nottingham Forest currently.", "Nottingham Forest"),
    ("Fulham FC starters this season?", "Fulham FC"),
    ("Who suits up for Sheffield United this season?", "Sheffield United"),
    ("Luton Town current footballers?", "Luton Town"),
])
def test_query_router_indirect_requests(query_router: QueryRouter, query_str: str, expected_team: str):
    result = query_router.analyze(query_str, history_str="")
    assert result.is_squad_query is True
    assert result.team_name == expected_team
    assert result.refer_to_current_squad is True 