from typing import List, Optional, Tuple
import gradio as gr
from llama_index.llms.openrouter import OpenRouter
from app.services.football_api_client import FootballAPIClient
from app.services.player_details_fetcher import PlayerDetailFetcher
from app.services.squad_fetcher import SquadFetcher
from app.settings import settings
from app.services.query_router import QueryRouter
from app.models import PlayerDetail, PlayerInSquad

try:
    llm = OpenRouter(
        api_key=settings.openrouter_api_key,
        model=settings.model_name,
        temperature=0.0,
    )
    api_client = FootballAPIClient(api_key=settings.football_api_key, api_host=settings.football_api_host)
    query_router = QueryRouter(llm=llm)
    squad_fetcher = SquadFetcher(api_client=api_client)
    player_detail_fetcher = PlayerDetailFetcher(api_client=api_client)
except Exception as e:
    print(f"FATAL: Could not initialize components. Check your .env file and API keys. Error: {e}")
    exit()

def format_squad_details(team_name: str, players: List[Tuple[PlayerInSquad, Optional[PlayerDetail]]]) -> str:
    """Formats the final squad list into a Markdown table."""
    if not players:
        return f"Could not retrieve any player details for **{team_name}**."

    header = f"### Squad List for {team_name}\n\n"
    table = "| First Name | Last Name | Date of Birth | Position |\n"
    table += "|------------|-----------|---------------|----------|\n"

    for squad_info, detail_info in players:
        first_name = "N/A"
        last_name = f"({squad_info.name})"
        dob = "N/A"

        if detail_info:
            first_name = detail_info.firstname
            last_name = detail_info.lastname
            if detail_info.birth and detail_info.birth.date:
                dob = detail_info.birth.date

        position = squad_info.position
        table += f"| {first_name} | {last_name} | {dob} | {position} |\n"

    return header + table

def answer(message, history):
    """
    Handles a user query by orchestrating the components and streaming the response.
    """
    yield "🧠 Analyzing your request..."
    try:
        analysis = query_router.analyze(message, history_str="\n".join([msg[0] for msg in history ]))
    except Exception as e:
        print(f"LLM analysis failed: {e}")
        yield "Sorry, I had trouble understanding your request. The AI model may be temporarily unavailable."
        return

    if not analysis.is_squad_query or not analysis.team_name:
        yield "I am a specialized bot that provides football squad information. Please ask a question like 'Who is in the Manchester City squad?'"
        return

    team_name = analysis.team_name
    yield f"✅ Request understood. Searching for squad information for **{team_name}**..."

    squad_list = squad_fetcher.get_squad_player_info(team_name )

    team_name_used = team_name
    if not squad_list and analysis.simple_team_name:
        yield f"Could not find squad for '{team_name}'. Trying simplified name '{analysis.simple_team_name}'..."
        team_name_used = analysis.simple_team_name
        squad_list = squad_fetcher.get_squad_player_info(analysis.simple_team_name)

    if squad_list is None:
        yield f"⚠️ Sorry, I could not find a team named '{team_name}'. Please check the name and try again."
        return
    if not squad_list:
        yield f"ℹ️ Found the team **{team_name}**, but could not retrieve the squad list. They may not have a registered squad for the current season."
        return

    yield f"Found {len(squad_list)} players. Fetching details... (this may take a moment)"

    full_player_data = []
    if settings.is_trial_football_api_key:
        squad_list = squad_list[:5]  # Limit to 5 players for trial API key to limit requests

    #todo run in prallel
    for player in squad_list:
        details = player_detail_fetcher.get_details_for_player(player.id)
        full_player_data.append((player, details))

    final_response = format_squad_details(team_name_used, full_player_data)
    yield final_response


demo = gr.ChatInterface(
    fn=answer,
    title="TransferRoom Squad Bot",
    description="Ask for a Premier League team's squad list. Example: 'Please list the current squad for Arsenal.'",
    chatbot=gr.Chatbot(
        height=500,
        placeholder="Ask me about a team's squad...",
        show_label=False,
    ),
    textbox=gr.Textbox(
        placeholder="Type your question here and press Enter...",
        container=False,
        scale=7
    ),
    examples=[
        ["Please list all the current senior squad members for the Manchester United men's team"],
        ["show me the liverpool squad"],
        ["who is on the chelsea team?"],
        ["who won the world cup in 2014?"]
    ],
    theme="soft",
    cache_examples=False,
)

if __name__ == "__main__":
    demo.launch()