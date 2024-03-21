FROM python:3.12-slim as build

WORKDIR /opt/users_info
ENV PATH /opt/users_info/.venv/bin/:$PATH

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY poetry.lock pyproject.toml ./

RUN python -m pip install --no-cache-dir poetry==1.7.1 \
    && poetry config virtualenvs.in-project true \
    && poetry install --no-interaction --without=test --no-ansi

FROM build AS app

COPY --from=build /opt/users_info /opt/users_info
COPY src ./src
COPY  start.sh .

ENTRYPOINT [ "bash", "/opt/users_info/start.sh" ]
