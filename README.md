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
2.  **Handling Out of scope questions:** The system is designed to provide current squad information. If a user query asks for something that is out of scope, they will be notified.
3.  **Team ID Resolution:** The extracted team name is used to query the Football API to find the corresponding team ID.
4.  **Squad Retrieval:** With the team ID, the application fetches the list of players in the squad from the Football API.
5.  **Player Detail Enrichment:** For each player in the squad, individual player details (like date of birth) are fetched from the Football API.
6.  **Response Formatting:** The collected player information is formatted into a clear, readable table and presented to the user via the chat interface.

## Setup and Installation

### Prerequisites

*   Python 3.13
*   `uv` for dependency management
*   Docker (optional, for containerised deployment)

### API Keys

This application requires API keys for the following services:

*   **OpenRouter:** For LLM access. Obtain your API key from [OpenRouter](https://openrouter.ai/).
*   **api-sports.io Football API:** For football data. Obtain your API key from [api-football.com](https://www.api-football.com).
*   **Langfuse:** (Optional) For observability and tracing of LLM calls. Obtain your API keys from [Langfuse](https://langfuse.com/).

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

### Environment Variables

Create a `.env` file in the root directory of the project with the following variables:
```
OPENROUTER_API_KEY="your_openrouter_api_key_here"
FOOTBALL_API_KEY="your_football_api_key_here"

# Optional: Set to True if using a trial API key to limit requests
IS_TRIAL_FOOTBALL_API_KEY=True

# Optional: For Langfuse tracing
# LANGFUSE_PUBLIC_KEY="your_langfuse_public_key_here"
# LANGFUSE_SECRET_KEY="your_langfuse_secret_key_here"
# LANGFUSE_HOST="https://cloud.langfuse.com" # Or your self-hosted instance
```

Remove unused variables and comments from env file
## Running the Application

Once the dependencies are installed and the `.env` file is configured, run the application:

```bash
python main.py
```
This will launch a Gradio web interface, typically accessible at http://127.0.0.1:7860.

### Running with Docker

Alternatively, you can run the application using Docker. Ensure you have Docker installed.

1.  **Build the Docker image:**
    ```bash
    docker build -t football-squad-app .
    ```
2.  **Run the Docker container:**
    You can pass your environment variables directly or use an `.env` file.
    Using `-e` flags (replace with your actual keys):
    ```bash
    docker run -p 80:80 \
      -d \
      -e OPENROUTER_API_KEY="your_openrouter_api_key_here" \
      -e FOOTBALL_API_KEY="your_football_api_key_here" \
      -e IS_TRIAL_FOOTBALL_API_KEY=True \
      -e LANGFUSE_PUBLIC_KEY="your_langfuse_public_key_here" \
      -e LANGFUSE_SECRET_KEY="your_langfuse_secret_key_here" \
      -e LANGFUSE_HOST="https://cloud.langfuse.com" \
      football-squad-app
    ```
    Or, using an `.env` file (ensure your `.env` file is in the same directory where you run the command):
    ```bash
    docker run -p 80:80 --env-file .env -d football-squad-app
    ```
    The application will be accessible at `http://localhost:7860`.

## Evaluation Tests

The project includes a suite of integration evaluation tests using `pytest` to ensure the `QueryRouter` component correctly interprets various user queries. These tests cover different scenarios, including simple team names, indirect requests, handling typos, and identifying out-of-scope or non-current squad queries.

The tests are located in the `evaluation/` directory.

### Running the Tests

To run the evaluation tests, navigate to the project root directory and execute `pytest`:

```bash
pytest
```

This command will discover and run all tests within the `evaluation/` directory, providing feedback on the `QueryRouter`'s performance.

## Important Notes

*   If you are using a trial API key for api-football.com, the results might be outdated or limited in scope due to API restrictions. The application includes a mechanism to limit player detail fetches to 5 players when `IS_TRIAL_FOOTBALL_API_KEY` is set to `True`.
*   The solution prioritises deterministic and accurate data retrieval over versatility in query types. It is specifically designed for squad information.
