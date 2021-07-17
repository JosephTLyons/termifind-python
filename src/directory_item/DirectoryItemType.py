from __future__ import annotations

from enum import Enum, auto
from pathlib import Path
from typing import Any

from Settings import Settings


class DirectoryItemType(Enum):
    APPLICATION = auto()
    DIRECTORY = auto()
    FILE = auto()
    SYMLINK = auto()

    def __lt__(self, other: DirectoryItemType) -> bool:
        self_sort_value: int = DIRECTORY_ITEM_TYPE_ATTRIBUTE_DICTIONARY[self]["sort_value"]
        other_sort_value: int = DIRECTORY_ITEM_TYPE_ATTRIBUTE_DICTIONARY[other]["sort_value"]

        return self_sort_value < other_sort_value


class UnknownDirectoryItemType(Exception):
    pass


def get_directory_item_type(path: Path) -> DirectoryItemType:
    if path.is_dir():
        # Applications are folders on Mac, so `is_dir()` returns `True` for them, which is why
        # this is nested in this area
        if str(path.name).endswith(".app"):
            return DirectoryItemType.APPLICATION

        return DirectoryItemType.DIRECTORY
    elif path.is_file():
        return DirectoryItemType.FILE
    elif path.is_symlink():
        return DirectoryItemType.SYMLINK
    else:
        # TODO: Should this be a different error?
        raise UnknownDirectoryItemType(f"{path} is not an application, directory, file, or symlink")


DIRECTORY_ITEM_TYPE_ATTRIBUTE_DICTIONARY: dict[DirectoryItemType, dict[str, Any]] = {
    DirectoryItemType.APPLICATION: {
        "style": Settings.APPLICATION_STYLE,
        "symbol": Settings.APPLICATION_SYMBOL,
        "sort_value": 1,
    },
    DirectoryItemType.DIRECTORY: {
        "style": Settings.DIRECTORY_STYLE,
        "symbol": Settings.DIRECTORY_SYMBOL,
        "sort_value": 0,
    },
    DirectoryItemType.FILE: {
        "style": Settings.FILE_STYLE,
        "symbol": Settings.FILE_SYMBOL,
        "sort_value": 2,
    },
    DirectoryItemType.SYMLINK: {
        "style": Settings.SYMLINK_STYLE,
        "symbol": Settings.SYMLINK_SYMBOL,
        "sort_value": 3,
    },
}
