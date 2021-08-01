from __future__ import annotations

import bisect
from pathlib import Path
from typing import Optional

from Settings import Settings
from src.directory_item.directory_item import DirectoryItem, DirectoryItemMetaData
from src.directory_item.directory_item_type import DirectoryItemType


class DirectoryContainer:
    def __init__(self, path: Path, selected_item: Optional[Path]=None) -> None:
        self.path: Path = path
        self.has_permission_error: bool = False
        self.directory_items: list[DirectoryItem] = self.__get_directory_items()
        self.selected_item = selected_item

        if self.selected_item:
            self.selected_item_index: int = self.__get_index_of_selected_directory_item()
        else:
            self.selected_item_index = 0

    def __str__(self) -> str:
        path_name: str = self.path.name

        # Calling `name` on a `Path` object that is just the root directory produces an empty
        # string, so simply call the `str()` on the path in that case
        if path_name:
            name: str = path_name
        else:
            name = str(self.path)

        if self.has_permission_error:
            additional_information: str = "Permission Error"
        else:
            additional_information = str(len(self.directory_items))

        name += f" ({additional_information})"

        return name

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

    def get_selected_directory_item(self) -> DirectoryItem:
        return self.directory_items[self.selected_item_index]

    def get_item_related_to_selected_item(self) -> DirectoryContainer | DirectoryItemMetaData:
        directory_item: DirectoryItem = self.get_selected_directory_item()

        if directory_item.directory_item_type == DirectoryItemType.DIRECTORY:
            return DirectoryContainer(directory_item.path)

        return directory_item.metadata

    def __get_directory_items(self) -> list[DirectoryItem]:
        directory_items: list[DirectoryItem] = []

        try:
            for item in self.path.iterdir():
                directory_item: DirectoryItem = DirectoryItem(item)

                if directory_item.name in Settings.FILE_ITEM_EXCLUSION_LIST:
                    continue

                if directory_item.is_hidden_file and not Settings.SHOULD_SHOW_HIDDEN_FILES:
                    continue

                bisect.insort(directory_items, directory_item)
        except PermissionError:
            self.has_permission_error = True

        return directory_items

    def __get_index_of_selected_directory_item(self) -> int:
        for index, directory_item in enumerate(self.directory_items):
            if directory_item.path == self.selected_item:
                return index

        return 0
