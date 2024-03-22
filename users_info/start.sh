#!/bin/bash

set -eo pipefail

#alembic upgrade head
#exec скрипт для создания пользователей

exec uvicorn src.main:app --host 0.0.0.0 --port "$API_PORT"
