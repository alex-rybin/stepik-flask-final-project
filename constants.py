from enum import Enum


class StrEnum(str, Enum):
    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def get_choices(cls) -> list[tuple[str, str]]:
        return [(x.value, x.value.title()) for x in cls]


class DifficultyOptions(StrEnum):
    EASY = 'Легко'
    MEDIUM = 'Средне'
    HARD = 'Сложно'


GAME_DESCRIPTION = (
    'Рядом с вами появился Фантом алгебры. Он не очень добр, но из-за проклятия не может тронуть '
    'того, кто верно решает математические примеры. Решайте примеры вовремя, чтобы выжить! '
    'На каждый пример даётся 10 секунд.'
)

LOST_GAME_MESSAGE = (
    'Фантом алгебры съел вас :('
)

LIVES = 3
