from pathlib import Path
from Settings import Settings

from src.DirectoryItem.DirectoryItemType import DirectoryItemType


class DirectoryItem:
    def __init__(self, path: Path) -> None:
        self.path: Path = path
        self.name: str = self.path.name
        self.is_hidden_file: bool = self.name.startswith(".")

        if not Settings.SHOULD_SHOW_FILE_EXTENSIONS and not self.is_hidden_file:
            self.name = self.name.split(".")[0]

        self.directory_item_type = DirectoryItemType.get_directory_item_type(self.path)

    def __str__(self) -> str:
        if Settings.SHOULD_SHOW_DIRECTORY_ITEM_TYPE:
            return f"({self.directory_item_type.symbol}) {self.name}"

        return self.name
