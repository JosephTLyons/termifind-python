from enum import Enum


class LayoutRegion(Enum):
    LOWER = "Lower"
    UPPER = "Upper"
    LEFT = "Left"
    MIDDLE = "Middle"
    RIGHT = "Right"

    def __str__(self):
        return self.value
