import datetime
from typing import Optional
from llama_index.core.llms import LLM
from llama_index.core.prompts import PromptTemplate
from pydantic import BaseModel, Field


class QueryAnalysis(BaseModel):
    """Data model for analyzing the user's query."""
    is_squad_query: bool = Field(
        description="True if the user is asking for a list of players in a specific football team's squad, False otherwise."
    )
    team_name: Optional[str] = Field(
        default=None,
        description="The full, official or commonly recognized name of the football team mentioned in the query. Example: 'Manchester United', 'FC Barcelona'."
    )
    simple_team_name: Optional[str] = Field(
        default=None,
        description="A simplified, common name for the football team, often without prefixes like 'FC' or 'Real', or suffixes like 'United', 'City'. Example: 'Barcelona' for 'FC Barcelona', 'Madrid' for 'Real Madrid', 'United' for 'Manchester United'."
    )
    refer_to_current_squad: bool = Field(
        default=True, 
        description="True if the user is asking for the current squad (or no specific year is mentioned, implying current), False if they are explicitly asking for a historical season or year (e.g., '1999 squad', 'players from 2005')."
    )


class QueryRouter:
    """
    Component 1: Analyzes the user's query to determine intent and extract the team name.
    """
    def __init__(self, llm: LLM):
        self.llm = llm
        self.prompt = PromptTemplate(
            "Current year: {current_year}\n"
            "Conversation history: {history}\n"
            "You are an expert system that analyzes user queries about football. "
            "Your task is to determine if the user is asking for a team's squad list. "
            "If they are, extract the full team name, a simplified version of the name, "
            "and indicate if they are asking for the current squad or a historical one.\n"
            "The team_name should be the most complete or common name. The simple_team_name should be a shorter, "
            "more concise version, often just the city or the most distinguishing part of the name.\n"
            "The 'refer_to_current_squad' field should be true if the query refers to the current year ({current_year}), "
            "or does not specify a year, assuming it's for the current squad. "
            "It should be false if the query explicitly mentions a year or season *other than the current year ({current_year})*.\n"
            "Examples:\n"
            "- Query: 'who is on the manchester city team?' -> {{\"is_squad_query\": true, \"team_name\": \"Manchester City\", \"simple_team_name\": \"Man City\", \"refer_to_current_squad\": true}}\n" 
            "- Query: 'show me the arsenal squad' -> {{\"is_squad_query\": true, \"team_name\": \"Arsenal\", \"simple_team_name\": \"Arsenal\", \"refer_to_current_squad\": true}}\n" 
            "- Query: 'FC Barcelona players' -> {{\"is_squad_query\": true, \"team_name\": \"FC Barcelona\", \"simple_team_name\": \"Barcelona\", \"refer_to_current_squad\": true}}\n" 
            "- Query: 'Real Madrid squad list' -> {{\"is_squad_query\": true, \"team_name\": \"Real Madrid\", \"simple_team_name\": \"Real Madrid\", \"refer_to_current_squad\": true}}\n" 
            "- Query: 'Give me a sense of Man City’s current roster' -> {{\"is_squad_query\": true, \"team_name\": \"Manchester City\", \"simple_team_name\": \"Man City\", \"refer_to_current_squad\": true}}\n" 
            "- Query: 'who was in the 1999 Manchester United squad?' -> {{\"is_squad_query\": true, \"team_name\": \"Manchester United\", \"simple_team_name\": \"Man Utd\", \"refer_to_current_squad\": false}}\n" 
            "- Query: 'who won the world cup?' -> {{\"is_squad_query\": false, \"team_name\": null, \"simple_team_name\": null, \"refer_to_current_squad\": true}}\n" 
            "User query: {query_str}\n"
        )

    def analyze(self, query: str, history_str: str) -> QueryAnalysis:
        """Uses the LLM to analyze the query and return a structured QueryAnalysis object."""

        current_year = datetime.datetime.now().year

        return self.llm.structured_predict(
            QueryAnalysis,
            self.prompt,
            query_str=query,
            history=history_str,
            current_year=current_year, 
        )