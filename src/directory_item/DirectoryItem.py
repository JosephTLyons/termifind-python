from __future__ import annotations

from pathlib import Path

from Settings import Settings
from src.directory_item.DirectoryItemType import get_directory_item_type, get_directory_item_type_symbol


class DirectoryItem:
    def __init__(self, path: Path) -> None:
        self.path: Path = path
        self.name: str = self.path.name
        self.is_hidden_file: bool = self.name.startswith(".")

        if not Settings.SHOULD_SHOW_FILE_EXTENSIONS and not self.is_hidden_file:
            self.name = self.name.split(".")[0]

        self.directory_item_type = get_directory_item_type(self.path)

    def __str__(self) -> str:
        if Settings.SHOULD_SHOW_DIRECTORY_ITEM_TYPE:
            directory_item_symbol = get_directory_item_type_symbol(self.directory_item_type)
            return f"({directory_item_symbol}) {self.name}"

        return self.name

    def __lt__(self, other: DirectoryItem) -> bool:
        if Settings.SHOULD_SORT_CASE_SENSITIVE:
            return self.name < other.name

        return self.name.lower() < other.name.lower()
