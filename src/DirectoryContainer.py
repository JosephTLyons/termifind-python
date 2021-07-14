from __future__ import annotations

import bisect
from pathlib import Path
from typing import Optional

from Settings import Settings
from src.directory_item.DirectoryItem import DirectoryItem
from src.directory_item.DirectoryItemType import DirectoryItemType


class DirectoryContainer:
    def __init__(self, path: Path) -> None:
        self.path: Path = path
        self.directory_items: list[DirectoryItem] = self.get_directory_items()
        self.selected_item_index: int = 0

    def move_down(self) -> None:
        if self.selected_item_index == len(self.directory_items) - 1:
            self.selected_item_index = 0
        else:
            self.selected_item_index += 1

    def move_up(self) -> None:
        if self.selected_item_index == 0:
            self.selected_item_index = len(self.directory_items) - 1
        else:
            self.selected_item_index -= 1

    def get_directory_items(self) -> list[DirectoryItem]:
        directory_items: list[DirectoryItem] = []

        for item in self.path.iterdir():
            directory_item: DirectoryItem = DirectoryItem(item)

            if directory_item.is_hidden_file and not Settings.SHOULD_SHOW_HIDDEN_FILES:
                continue

            bisect.insort(directory_items, directory_item)

        return directory_items

    def get_next_directory_container(self) -> Optional[DirectoryContainer]:
        directory_item = self.directory_items[self.selected_item_index]

        if directory_item.directory_item_type == DirectoryItemType.DIRECTORY:
            return DirectoryContainer(directory_item.path)

        return None
