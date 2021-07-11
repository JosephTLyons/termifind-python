from enum import Enum, auto


class LayoutRegion(Enum):
    LOWER = auto()
    UPPER = auto()
    LEFT = auto()
    MIDDLE = auto()
    RIGHT = auto()

    @property
    def __name__(self) -> str:
        return self.name.title()
