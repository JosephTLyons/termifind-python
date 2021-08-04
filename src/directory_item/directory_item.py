from __future__ import annotations
import datetime
import os
from pathlib import Path
from typing import Any, Callable

import humanize  # type: ignore

from settings import Settings
from src.directory_item.directory_item_type import get_directory_item_type, get_directory_item_type_attributes


class DirectoryItem:
    def __init__(self, path: Path) -> None:
        self.path: Path = path
        self.name: str = self.path.name
        self.is_hidden_file: bool = self.name.startswith(".")

        if not Settings.SHOULD_SHOW_FILE_EXTENSIONS and not self.is_hidden_file:
            self.name = self.name.split(".")[0]

        self.directory_item_type = get_directory_item_type(self.path)

        self.metadata = DirectoryItemMetaData(self)


    def __str__(self) -> str:
        if Settings.SHOULD_SHOW_DIRECTORY_ITEM_TYPE:
            directory_item_symbol = get_directory_item_type_attributes(self.directory_item_type).symbol
            return f"({directory_item_symbol}) {self.name}"

        return self.name

    def __lt__(self, other: DirectoryItem) -> bool:
        if Settings.SHOULD_SORT_CASE_SENSITIVE:
            self_name: str = self.name
            other_name: str = other.name
        else:
            self_name = self.name.lower()
            other_name = other.name.lower()

        if Settings.SHOULD_GROUP_ITEMS_BY_TYPE:
            return (self.directory_item_type, self_name) < (other.directory_item_type, other_name)

        return self_name < other_name


# This class was it its own module, but was moved into this class to resolve a circular import
# TODO: Figure out to solve the circular import issue later
class DirectoryItemMetaData:
    def __init__(self, directory_item: DirectoryItem) -> None:
        self.directory_item: DirectoryItem = directory_item
        file_size_in_bytes = self.__get_file_metadata(directory_item.path, os.path.getsize)
        self.size: str = humanize.naturalsize(file_size_in_bytes) if file_size_in_bytes else "0 Bytes"
        self.created_time: float = self.__get_file_metadata(directory_item.path, os.path.getctime)
        self.modified_time: float = self.__get_file_metadata(directory_item.path, os.path.getmtime)
        self.accessed_time: float = self.__get_file_metadata(directory_item.path, os.path.getatime)


    def __str__(self) -> str:
        return f"{self.directory_item.name} Metadata"


    def __get_file_metadata(self, path: Path, metadate_function: Callable[[Any], Any]) -> Any:
        try:
            return metadate_function(path)
        except FileNotFoundError:
            pass

        return None


    def get_file_metadata_dictionary(self) -> dict[str, Any]:
        metadata_dictionary: dict[str, Any] = {
            "Size": self.size,
            "Created": self.__get_formatted_datetime_string_from_timestamp(self.created_time),
            "Modified": self.__get_formatted_datetime_string_from_timestamp(self.modified_time),
            "Accessed": self.__get_formatted_datetime_string_from_timestamp(self.accessed_time),
        }

        return metadata_dictionary

    def __get_formatted_datetime_string_from_timestamp(self, timestamp: float) -> str:
        datetime_object = datetime.datetime.fromtimestamp(timestamp)
        datetime_format_string = "%b %d, %Y %I:%M %p"

        return datetime_object.strftime(datetime_format_string)
