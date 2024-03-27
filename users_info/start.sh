#!/bin/bash

set -eo pipefail

python cli/run.py migrate

if [[ "$MOCK" == "True" ]]; then python cli/run.py create --mock; else python cli/run.py create; fi

exec uvicorn src.main:app --host 0.0.0.0 --port "$USERS_API_PORT"
