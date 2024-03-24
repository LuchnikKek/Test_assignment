from enum import StrEnum, auto


class Gender(StrEnum):
    """
    Перечисление всех полов.
    В соответствии с ISO 5218: https://en.wikipedia.org/wiki/ISO/IEC_5218

    Стандарт предусматривает ещё значение 'NOT KNOWN', означающее, что пол не указан.
    Его решил реализовать как NULL в базе, чтобы избежать двойственного значения.
    """

    MALE = auto()
    FEMALE = auto()
    NOT_APPLICABLE = auto()


class FriendRequestStatus(StrEnum):
    """Перечисление всех состояний запроса дружбы.

    Значения:
        'requested': запрос отправлен.
        'accepted': запрос принят.
        'declined': запрос отклонён.
    """

    REQUESTED = auto()
    ACCEPTED = auto()
    DECLINED = auto()
