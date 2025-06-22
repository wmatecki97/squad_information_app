import pytest
import logging
from app.services.query_router import QueryRouter
from app.settings import Settings
from llama_index.llms.openrouter import OpenRouter

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

settings = Settings()

if not settings.openrouter_api_key:
    pytest.skip("OPENROUTER_API_KEY not set, skipping LLM integration tests.", allow_module_level=True)
if not settings.model_name:
    pytest.skip("MODEL_NAME not set, skipping LLM integration tests.", allow_module_level=True)

try:
    llm = OpenRouter(
        api_key=settings.openrouter_api_key,
        model=settings.model_name,
        temperature=0.0,
    )
except Exception as e:
    pytest.fail(f"Failed to initialize OpenRouter LLM. Error: {e}")

@pytest.fixture(scope="module")
def query_router():
    return QueryRouter(llm=llm)
