from __future__ import annotations
from enum import Enum, auto
from pathlib import Path


class DirectoryItemType(Enum):
    FILE = auto()
    DIRECTORY = auto()
    SYMLINK = auto()

    @property
    def symbol(self) -> str:
        return self.name[0]

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
            raise Exception(f"Something is not right, {path} is not a directory, file, or symlink")
