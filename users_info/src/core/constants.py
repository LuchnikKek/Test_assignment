from enum import StrEnum, auto
from pathlib import Path


class Gender(StrEnum):
    """Перечисление всех полов.

    Значения:
        'MALE': Мужчина.
        'FEMALE': Женщина.
        'NOT_KNOWN': Неизвестно. Применяется в случаях, когда пол не был указан пользователем при регистрации.
        'NOT_APPLICABLE': Неприменимо. В повседневных задачах не используется. Фундамент, на всякий случай.

    Подробнее: ISO 5218: https://en.wikipedia.org/wiki/ISO/IEC_5218
    """

    MALE = auto()
    FEMALE = auto()
    NOT_KNOWN = auto()
    NOT_APPLICABLE = auto()


class FriendRequestStatus(StrEnum):
    """Перечисление всех состояний запроса дружбы.

    Значения:
        'REQUESTED': Запрос отправлен.
        'ACCEPTED': Запрос принят.
        'DECLINED': Запрос отклонён.
    """

    REQUESTED = auto()
    ACCEPTED = auto()
    DECLINED = auto()


ROOT_PATH: Path = Path(__file__).parent.parent.parent.parent
ENV_FILEPATH: Path = ROOT_PATH / ".env"
