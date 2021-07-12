from __future__ import annotations
from enum import Enum, auto
from pathlib import Path

from Settings import Settings


class DirectoryItemType(Enum):
    APPLICATION = auto()
    DIRECTORY = auto()
    FILE = auto()
    SYMLINK = auto()

    @property
    def symbol(self) -> str:
        if self == DirectoryItemType.APPLICATION:
            return Settings.APPLICATION_SYMBOL
        elif self == DirectoryItemType.DIRECTORY:
            return Settings.DIRECTORY_SYMBOL
        elif self == DirectoryItemType.FILE:
            return Settings.FILE_SYMBOL
        elif self == DirectoryItemType.SYMLINK:
            return Settings.SYMLINK_SYMBOL
        else:
            raise ValueError(f"Unknown DirectoryItemType: {self}")

    @staticmethod
    def get_directory_item_type(path: Path) -> DirectoryItemType:
        if path.is_dir():
            # Applications are folders on Mac, so `is_dir()` returns `True` for them
            if str(path.name).endswith(".app"):
                return DirectoryItemType.APPLICATION

            return DirectoryItemType.DIRECTORY
        elif path.is_file():
            return DirectoryItemType.FILE
        elif path.is_symlink():
            return DirectoryItemType.SYMLINK
        else:
            # TODO: Fix this exception later
            raise ValueError(f"{path} is not a directory, file, or symlink")
