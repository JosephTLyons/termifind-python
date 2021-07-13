from enum import Enum, auto


# Delete?
class DirectoryItemState(Enum):
    DIRECTORY_IN_PATH = auto()
    SELECTED = auto()
    UNSELECTED = auto()
