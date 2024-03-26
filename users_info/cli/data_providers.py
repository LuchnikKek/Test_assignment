# Пример запроса одного имени: https://api.agify.io/?name=michael
# Пример запроса нескольких имён: https://api.agify.io?name[]=michael&name[]=matthew&name[]=jane
from http import HTTPStatus
from itertools import batched

import requests
import json
from typing import Iterable

from config import *

logger.setLevel(LOG_LVL)
ch.setFormatter(formatter)
logger.addHandler(ch)


def _format_params(names: Iterable) -> str:
    """Форматирует список имён в query-параметры."""
    return "?" + "&".join(["name[]=%s" % name for name in names])


async def _process_request(url: str, params: str) -> list:
    """
    Отправляет запрос, возвращает JSON-ответ.
    Если статус не 200 - возвращает пустой список.
    """
    response = requests.get(url + params)

    if not response.status_code == HTTPStatus.OK:
        logger.error("Ошибка от API: %s" % response.text)
        return []

    return response.json()


async def _get_ages(params: str) -> list:
    """Возвращает список возрастов. Если возраст не определён - в списке будет None."""
    data = await _process_request(AGIFY_URL, params)
    logger.info("Получены данные по возрастам: %s", data)
    return [person.get("age") for person in data]


async def _get_genders(params: str) -> list:
    """Возвращает список полов. Если пол не определён - в списке будет None."""
    data = await _process_request(GENDERIZE_URL, params)
    logger.info("Получены данные по полам: %s", data)
    return [person.get("gender").upper() for person in data]


async def _get_nationalities(params: str) -> list:
    """Возвращает список национальностей. Если национальность не определена - в списке будет None."""
    data = await _process_request(NATIONALIZE_URL, params)
    logger.info("Получены данные по национальностям: %s", data)

    nationalities = []

    for person in data:
        person_countries = person.get("country")
        nationalities.append(person_countries[0].get("country_id") if len(person_countries) > 0 else None)

    return nationalities


def _to_list_of_dicts(columns: Iterable, values: Iterable[Iterable]) -> list[dict]:
    """Превращает список колонок и списки значений для каждой в список словарей,
    где key из списка колонок, а value из соответствующего списка значений

    Пример:
        a = (1, 2)
        b = (3, 4)
        c = (5, 6)
        d = (7, 8)
        columns = ('key_a', 'key_b', 'key_c', 'key_d')
        _to_list_of_dicts(columns, zip(a, b, c, d))
        [{'key_a': 1, 'key_b': 3, 'key_c': 5, 'key_d': 7},
        {'key_a': 2, 'key_b': 4, 'key_c': 6, 'key_d': 8}]
    """
    return [dict(zip(columns, data)) for data in values]


async def query_data(firstnames: Iterable) -> list[dict]:
    """Запрашивает данные на интернет-ресурсах.

    Возвращает значения в формате списка словарей.
    Максимальный размер запроса к API определяется переменной MAX_API_BATCH_SIZE

    Пример:
        query_data(['john', 'bill'])
        [{'firstname': 'john', 'age': 73, 'gender': 'MALE', 'country_code': 'NG'},
        {'firstname': 'bill', 'age': 75, 'gender': 'MALE', 'country_code': 'CN'}]
    """
    columns = ("firstname", "age", "gender", "country_code")
    ages, genders, nationalities = [], [], []

    for names_batch in batched(firstnames, n=MAX_API_BATCH_SIZE):
        params_string = _format_params(names_batch)

        logger.info("Запрос данных по именам %s", names_batch)
        ages.extend(await _get_ages(params_string))
        genders.extend(await _get_genders(params_string))
        nationalities.extend(await _get_nationalities(params_string))
        logger.info("Данные успешно получены")

    return _to_list_of_dicts(columns=columns, values=zip(firstnames, ages, genders, nationalities))


async def get_data():
    """Возвращает список людей и информацию по ним из стороннего API.

    Список людей описывается в файле, заданном переменной NAMES_JSON_FILEPATH.
    """
    logger.info("Получение данных")

    with open(NAMES_JSON_FILEPATH) as file:
        person_data: list[dict] = json.load(file)

    firstnames = [person.get("firstname") for person in person_data]
    api_response_data = await query_data(firstnames)
    [person.update(response) for person, response in zip(person_data, api_response_data)]

    logger.info("Получение данных завершено")
    logger.debug("Полученные данные: %s" % person_data)

    return person_data


async def get_mock_data():
    """Возвращает список людей и информацию по ним из файла MOCK_DATA_JSON_FILEPATH."""
    logger.info("Получение mock данных")

    with open(MOCK_DATA_JSON_FILEPATH) as file:
        data: list[dict] = json.load(file)

    logger.info("Получение mock данных завершено")
    logger.debug("Полученные данные: %s" % data)

    return data
