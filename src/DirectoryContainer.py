from __future__ import annotations

import bisect
from pathlib import Path
from typing import Optional

from rich.panel import Panel
from rich.text import Text

from Settings import Settings
from src.directory_item.DirectoryItem import DirectoryItem
from src.directory_item.DirectoryItemType import DirectoryItemType, get_directory_item_type_style


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

    def get_directory_container_panel(self, should_style_text: bool = True) -> Panel:
        item_name_texts: Text = self.__get_item_name_text(should_style_text)

        # Calling `name` on a `Path` object that is just the root directory produces an empty
        # string, so simply call the `str()` on the path in that case
        path_name = self.path.name

        if path_name:
            panel_title: str = path_name
        else:
            panel_title = str(self.path)

        panel_title += f" ({len(self.directory_items)})"

        return Panel(item_name_texts, title=panel_title, expand=True)

    def __get_item_name_text(self, should_style_text: bool) -> Text:
        item_name_text: Text = Text(no_wrap=True, overflow="ellipsis")

        for index, directory_item in enumerate(self.directory_items):
            if index == self.selected_item_index:
                selection_status: str = Settings.SELECTOR_SYMBOL
            else:
                selection_status = " " * len(Settings.SELECTOR_SYMBOL)

            item_name_text.append(f"{selection_status} ")

            if should_style_text:
                directory_item_type_color: Optional[str] = get_directory_item_type_style(directory_item.directory_item_type)
            else:
                directory_item_type_color = None

            item_name_text.append(f"{directory_item}\n", style=directory_item_type_color)

        return item_name_text
