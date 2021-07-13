from pathlib import Path
from typing import Optional

from rich.panel import Panel

from src.DirectoryContainer import DirectoryContainer
from src.ui.LayoutRegion import LayoutRegion
from src.file_utility_functions import get_list_of_parent_directories_from_path


class PathContainer:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.path_directories: list[Path] = get_list_of_parent_directories_from_path(path)
        self.path_directory_containers: list[DirectoryContainer] = [DirectoryContainer(path) for path in self.path_directories]

        self.set_visible_directory_containers()

    def set_visible_directory_containers(self) -> None:
        self.previous_directory_container: Optional[DirectoryContainer] = None
        self.current_directory_container: Optional[DirectoryContainer] = None
        self.next_directory_container: Optional[DirectoryContainer] = None

        if len(self.path_directory_containers) > 1:
            self.previous_directory_container = self.path_directory_containers[-2]

        if len(self.path_directory_containers) > 0:
            self.current_directory_container = self.path_directory_containers[-1]
            self.next_directory_container = self.current_directory_container.get_next_directory_container()

    def get_directory_container_panels_dictionary(self) -> dict[str, Panel]:
        panels_dictionary: dict[str, Panel] = {}

        if self.previous_directory_container:
            panels_dictionary[LayoutRegion.LEFT.name] = self.previous_directory_container.get_directory_container_panel()

        if self.current_directory_container:
            panels_dictionary[LayoutRegion.MIDDLE.name] = self.current_directory_container.get_directory_container_panel()

        if self.next_directory_container:
            panels_dictionary[LayoutRegion.RIGHT.name] = self.next_directory_container.get_directory_container_panel()

        return panels_dictionary
