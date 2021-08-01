from itertools import zip_longest
from pathlib import Path
from typing import Optional

from src.directory_container import DirectoryContainer
from src.directory_item.directory_item import DirectoryItemMetaData
from src.file_utility_functions import get_list_of_directories_from_path


class PathContainer:
    def __init__(self, path: Path) -> None:
        self.path = path
        directories_list: list[Path] = get_list_of_directories_from_path(path)
        path_and_selected_item_zip: zip_longest = zip_longest(directories_list, directories_list[1:])
        self.directory_containers: list[DirectoryContainer] = [
            DirectoryContainer(path, selected_item=selected_item) for path, selected_item in path_and_selected_item_zip

        ]

        self.previous_directory_container: Optional[DirectoryContainer] = None
        self.current_directory_container: Optional[DirectoryContainer] = None
        self.selected_item_contents_preview: Optional[DirectoryContainer | DirectoryItemMetaData] = None

        self.set_current_directory_containers()

    # Should this simply return the DirectoryContainers?
    def set_current_directory_containers(self) -> None:
        if len(self.directory_containers) > 1:
            self.previous_directory_container = self.directory_containers[-2]

        if len(self.directory_containers) > 0:
            self.current_directory_container = self.directory_containers[-1]
            self.selected_item_contents_preview = self.current_directory_container.get_item_related_to_selected_item()
