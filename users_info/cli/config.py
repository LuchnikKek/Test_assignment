import logging
import os

DB_USER = os.environ.get("USERS_PG_USER")
DB_PASSWORD = os.environ.get("USERS_PG_PASSWORD")
DB_HOST = os.environ.get("USERS_PG_HOST")
DB_PORT = os.environ.get("USERS_PG_PORT")
DB_NAME = os.environ.get("USERS_PG_DATABASE")
DSN = f"postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

MAX_API_BATCH_SIZE = 10
NAMES_JSON_FILEPATH = "cli/data/names.json"
MOCK_DATA_JSON_FILEPATH = "cli/data/mock_data.json"
AGIFY_URL = "https://api.agify.io"
GENDERIZE_URL = "https://api.genderize.io"
NATIONALIZE_URL = "https://api.nationalize.io"

DEBUG = os.environ.get("DEBUG") in ("True", "true", "1")

LOG_LVL = os.environ.get("LOG_LVL")

logger = logging.getLogger("cli")
logger.setLevel(LOG_LVL)

ch = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)
