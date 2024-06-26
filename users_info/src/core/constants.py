from enum import StrEnum
from pathlib import Path


class Gender(StrEnum):
    """Перечисление всех полов.

    Значения:
        'MALE': Мужчина.
        'FEMALE': Женщина.
        'NOT_KNOWN': Неизвестно. Применяется в случаях, когда пол не был указан пользователем при регистрации.
        'NOT_APPLICABLE': Неприменимо. В повседневных задачах не используется.

    Подробнее: ISO 5218: https://en.wikipedia.org/wiki/ISO/IEC_5218
    """

    MALE = "MALE"
    FEMALE = "FEMALE"
    NOT_KNOWN = "NOT_KNOWN"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class FriendRequestStatus(StrEnum):
    """Перечисление всех состояний запроса дружбы.

    Значения:
        'REQUESTED': Запрос отправлен.
        'ACCEPTED': Запрос принят.
        'DECLINED': Запрос отклонён.
    """

    REQUESTED = "REQUESTED"
    ACCEPTED = "ACCEPTED"
    DECLINED = "DECLINED"


ROOT_PATH: Path = Path(__file__).parent.parent.parent.parent
ENV_FILEPATH: Path = ROOT_PATH / ".env"
