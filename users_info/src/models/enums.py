from enum import StrEnum, auto


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
