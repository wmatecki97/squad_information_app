# Football Squad Bot

This application is a proof-of-concept designed to provide accurate football squad information for Premier League teams based on natural language queries. Users can ask questions like "Who is in the Manchester City squad?" and the bot will return a structured list of players including their first name, surname, date of birth, and playing position.

## Features

*   **Natural Language Understanding:** Leverages a Large Language Model (LLM) to interpret user queries and extract relevant information such as team names and intent.
*   **External API Integration:** Connects to a third-party Football API (api-sports.io) to fetch real-time team and player data.
*   **Data Retrieval:** Retrieves specific player details (first name, last name, date of birth, position) for each member of a requested squad.
*   **User-Friendly Interface:** Provides an interactive chat interface built with Gradio.

## How It Works

The application follows a multi-step process to answer user queries:

1.  **Query Analysis:** An LLM analyzes the user's natural language query to determine if it's a request for a team's squad and to extract the team's name.
2.  **Team ID Resolution:** The extracted team name is used to query the Football API to find the corresponding team ID.
3.  **Squad Retrieval:** With the team ID, the application fetches the list of players in the squad from the Football API.
4.  **Player Detail Enrichment:** For each player in the squad, individual player details (like date of birth) are fetched from the Football API.
5.  **Response Generation:** The collected player information is formatted into a clear, readable table and presented to the user via the chat interface.

## Setup and Installation

### Prerequisites

*   Python 3.13
*   `uv` (or `pip`) for dependency management

### API Keys

This application requires API keys for the following services:

*   **OpenRouter:** For LLM access. Obtain your API key from [OpenRouter](https://openrouter.ai/).
*   **api-sports.io Football API:** For football data. Obtain your API key from [api-sports.io](https://www.api-sports.io/football).

### Environment Variables

Create a `.env` file in the root directory of the project with the following variables:
```
OPENROUTER_API_KEY="your_openrouter_api_key_here"
FOOTBALL_API_KEY="your_football_api_key_here"
```

Optional: Set to True if using a trial API key to limit requests
```
IS_TRIAL_FOOTBALL_API_KEY=True
```


### Installation Steps

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  **Install dependencies using `uv`:**

    ```bash
    uv sync
    ```

## Running the Application

Once the dependencies are installed and the `.env` file is configured, run the application:

```bash
python main.py
```
This will launch a Gradio web interface, typically accessible at http://127.0.0.1:7860.
Important Notes

    If you are using a trial API key for api-sports.io, the results might be outdated or limited in scope due to API restrictions. The application includes a mechanism to limit player detail fetches to 5 players when IS_TRIAL_FOOTBALL_API_KEY is set to True.

    The solution prioritises deterministic and accurate data retrieval over versatility in query types. It is specifically designed for squad information.