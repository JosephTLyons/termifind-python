from __future__ import annotations
from pathlib import Path
from typing import Optional

from rich.panel import Panel

from Settings import Settings
from src.directory_item.DirectoryItem import DirectoryItem, DirectoryItemType


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

            directory_items.append(directory_item)

        if Settings.SHOULD_SORT_CASE_SENSITIVE:
            directory_items_sorted: list[DirectoryItem] = sorted(directory_items, key=lambda directory_item: directory_item.name)
        else:
            directory_items_sorted = sorted(directory_items, key=lambda directory_item: directory_item.name.lower())

        return directory_items_sorted

    def get_next_directory_container(self) -> Optional[DirectoryContainer]:
        for index, directory_item in enumerate(self.directory_items):
            if index == self.selected_item_index:
                if directory_item.directory_item_type == DirectoryItemType.DIRECTORY:
                    return DirectoryContainer(directory_item.path)

        return None

    def get_directory_container_panel(self) -> Panel:
        item_names: list[str] = []

        for index, directory_item in enumerate(self.directory_items):
            selected_status: str = "*" if index == self.selected_item_index else " "
            item_string: str = f"{selected_status} {directory_item}"
            item_names.append(item_string)

        item_names_string: str = "\n".join(item_names)

        # Calling `name` on a `Path` object that is just the root directory produces an empty
        # string, so simply call the `str()` on the path in that case
        path_name = self.path.name

        if path_name:
            panel_title: str = path_name
        else:
            panel_title = str(self.path)

        panel_title += f" ({len(self.directory_items)})"

        return Panel(item_names_string, title=panel_title, expand=True)
