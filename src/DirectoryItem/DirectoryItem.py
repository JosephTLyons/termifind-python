from pathlib import Path

from src.DirectoryItem.DirectoryItemType import DirectoryItemType


class DirectoryItem:
    def __init__(self, path: Path, is_selected: bool=False) -> None:
        self.path: Path = path
        self.name: str = self.path.name
        self.directory_item_type = DirectoryItemType.get_directory_item_type(self.path)

        self.is_hidden_file: bool = str(self.name).startswith(".")

    def __str__(self) -> str:
        return f"({self.directory_item_type.symbol}) {self.name}"
