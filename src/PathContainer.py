from pathlib import Path
from typing import Optional

from rich import print
from rich.panel import Panel

from src.DirectoryContainer import DirectoryContainer
from src.file_utility_functions import get_list_of_parent_directories_from_path


class PathContainer:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.path_directories: list[Path] = get_list_of_parent_directories_from_path(path)
        self.path_directory_containers: list[DirectoryContainer] = [DirectoryContainer(path) for path in self.path_directories]

    def print(self) -> None:
        print(Panel(f"Path: {self.path}", title="TermiFind", expand=True))

        if len(self.path_directory_containers) > 1:
            previous_directory_container: DirectoryContainer = self.path_directory_containers[-2]
            previous_directory_container.print()

        if len(self.path_directory_containers) > 0:
            current_directory_container: DirectoryContainer = self.path_directory_containers[-1]
            current_directory_container.print()

            next_directory_container: Optional[DirectoryContainer] = current_directory_container.get_next_directory_container()

            if next_directory_container:
                next_directory_container.print()
