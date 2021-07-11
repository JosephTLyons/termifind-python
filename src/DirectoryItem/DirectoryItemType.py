from __future__ import annotations
from enum import Enum, auto
from pathlib import Path

from settings import Settings


class DirectoryItemType(Enum):
    DIRECTORY = auto()
    FILE = auto()
    SYMLINK = auto()

    @property
    def symbol(self) -> str:
        if self == DirectoryItemType.DIRECTORY:
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
            return DirectoryItemType.DIRECTORY
        elif path.is_file():
            return DirectoryItemType.FILE
        elif path.is_symlink():
            return DirectoryItemType.SYMLINK
        else:
            # TODO: Fix this exception later
            raise ValueError(f"{path} is not a directory, file, or symlink")
