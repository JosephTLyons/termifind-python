from __future__ import annotations

from enum import Enum, auto
from pathlib import Path

from Settings import Settings


class DirectoryItemType(Enum):
    APPLICATION = auto()
    DIRECTORY = auto()
    FILE = auto()
    SYMLINK = auto()

    def __lt__(self, other: DirectoryItemType) -> bool:
        self_sort_value: int = get_directory_item_type_attributes(self).sort_value
        other_sort_value: int = get_directory_item_type_attributes(other).sort_value

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


class DirectoryItemTypeAttributes:
    def __init__(self, sort_value: int, style: str, symbol: str) -> None:
        self.sort_value: int = sort_value
        self.style: str = style
        self.symbol: str = symbol


def get_directory_item_type_attributes(directory_item_type: DirectoryItemType) -> DirectoryItemTypeAttributes:
    if directory_item_type == DirectoryItemType.APPLICATION:
        return DirectoryItemTypeAttributes(1, Settings.APPLICATION_STYLE,  Settings.APPLICATION_SYMBOL)
    elif directory_item_type == DirectoryItemType.DIRECTORY:
        return DirectoryItemTypeAttributes(0, Settings.DIRECTORY_STYLE, Settings.DIRECTORY_SYMBOL)
    elif directory_item_type == DirectoryItemType.FILE:
        return DirectoryItemTypeAttributes(2, Settings.FILE_STYLE, Settings.FILE_SYMBOL)
    elif directory_item_type == DirectoryItemType.SYMLINK:
        return DirectoryItemTypeAttributes(3, Settings.SYMLINK_STYLE, Settings.SYMLINK_SYMBOL)
    else:
        # TODO: Better error
        raise UnknownDirectoryItemType(f"Unknown {directory_item_type}")
