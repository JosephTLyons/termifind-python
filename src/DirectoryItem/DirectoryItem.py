from pathlib import Path
from settings import Settings

from src.DirectoryItem.DirectoryItemType import DirectoryItemType


class DirectoryItem:
    def __init__(self, path: Path) -> None:
        self.path: Path = path
        self.name: str = self.path.name
        self.is_hidden_file: bool = str(self.name).startswith(".")

        if not Settings.SHOULD_SHOW_FILE_EXTENSIONS and not self.is_hidden_file:
            self.name = self.name.split(".")[0]

        self.directory_item_type = DirectoryItemType.get_directory_item_type(self.path)

    def __str__(self) -> str:
        return f"({self.directory_item_type.symbol}) {self.name}"
