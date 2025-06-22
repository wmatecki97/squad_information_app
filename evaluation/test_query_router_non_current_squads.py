import pytest
from app.services.query_router import QueryRouter

@pytest.mark.parametrize("query_str", [
    "Who was in the Liverpool squad in 2018?",
    "Show me Chelsea’s 2020 squad",
    "What was Arsenal’s team lineup in 2006?",
    "Can you list Man City players from last season?",
    "Who were in Spurs squad back in 2015?",
    "Who played for Everton in the 90s?",
    "Aston Villa’s 2008 roster?",
    "Who featured for West Ham in 2010?",
    "Who was on Newcastle's team in 2002?",
    "Players that represented Fulham in 2009?",
    "Wolves squad during 2021 season?",
    "Crystal Palace players from last year?",
    "List Bournemouth’s 2016 players",
    "Leeds United 2004 team?",
    "Southampton's 2013/14 squad?",
    "Who was in Brighton’s team in 2022?",
    "Forest players in 1995?",
    "Who played for Brentford in 2020?",
    "Luton Town squad in 2005?",
    "Sheffield United players in 2007?",
])
def test_query_router_non_current_squads(query_router: QueryRouter, query_str: str):
    result = query_router.analyze(query_str, history_str="")
    assert result.refer_to_current_squad is False, f"Expected non-current squad query '{query_str}' to return refer_to_current_squad as False"