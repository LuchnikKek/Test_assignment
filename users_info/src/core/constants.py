from enum import StrEnum, auto
from pathlib import Path


class Gender(StrEnum):
    """Перечисление всех полов.

    Значения:
        'male': Мужчина.
        'female': Женщина.
        'not_known': Неизвестно. Применяется в случаях, когда пол не был указан пользователем при регистрации.
        'not_applicable': Неприменимо. В повседневных задачах не используется. Фундамент, на всякий случай.

    Подробнее: ISO 5218: https://en.wikipedia.org/wiki/ISO/IEC_5218
    """

    MALE = auto()
    FEMALE = auto()
    NOT_KNOWN = auto()
    NOT_APPLICABLE = auto()


class FriendRequestStatus(StrEnum):
    """Перечисление всех состояний запроса дружбы.

    Значения:
        'requested': Запрос отправлен.
        'accepted': Запрос принят.
        'declined': Запрос отклонён.
    """

    REQUESTED = auto()
    ACCEPTED = auto()
    DECLINED = auto()


ROOT_PATH: Path = Path(__file__).parent.parent.parent.parent
ENV_FILEPATH: Path = ROOT_PATH / ".env"


# Пример запроса одного имени: https://api.agify.io/?name=michael
# Пример запроса нескольких имён: https://api.agify.io?name[]=michael&name[]=matthew&name[]=jane
AGIFY_URL = "https://api.agify.io?"
GENDERIZE_URL = "https://api.genderize.io?"
NATIONALIZE_URL = "https://api.nationalize.io?"
