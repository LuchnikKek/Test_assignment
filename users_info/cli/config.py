import logging

MAX_API_BATCH_SIZE = 10
NAMES_JSON_FILEPATH = "cli/data/names.json"
MOCK_DATA_JSON_FILEPATH = "cli/data/mock_data.json"
AGIFY_URL = "https://api.agify.io"
GENDERIZE_URL = "https://api.genderize.io"
NATIONALIZE_URL = "https://api.nationalize.io"


LOG_LVL = logging.INFO
logger = logging.getLogger("cli")
ch = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
