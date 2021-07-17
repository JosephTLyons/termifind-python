from __future__ import annotations

from enum import Enum, auto
from pathlib import Path

from Settings import Settings


class DirectoryItemType(Enum):
    APPLICATION = auto()
    DIRECTORY = auto()
    FILE = auto()
    SYMLINK = auto()


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


def get_directory_item_type_symbol(directory_item_type: DirectoryItemType) -> str:
    if directory_item_type == DirectoryItemType.APPLICATION:
        return Settings.APPLICATION_SYMBOL
    elif directory_item_type == DirectoryItemType.DIRECTORY:
        return Settings.DIRECTORY_SYMBOL
    elif directory_item_type == DirectoryItemType.FILE:
        return Settings.FILE_SYMBOL
    elif directory_item_type == DirectoryItemType.SYMLINK:
        return Settings.SYMLINK_SYMBOL
    else:
        raise UnknownDirectoryItemType(f"Unknown DirectoryItemType: {directory_item_type}")


def get_directory_item_type_style(directory_item_type: DirectoryItemType) -> str:
    if directory_item_type == DirectoryItemType.APPLICATION:
        return Settings.APPLICATION_STYLE
    elif directory_item_type == DirectoryItemType.DIRECTORY:
        return Settings.DIRECTORY_STYLE
    elif directory_item_type == DirectoryItemType.FILE:
        return Settings.FILE_STYLE
    elif directory_item_type == DirectoryItemType.SYMLINK:
        return Settings.SYMLINK_STYLE
    else:
        raise UnknownDirectoryItemType(f"Unknown DirectoryItemType: {directory_item_type}")
