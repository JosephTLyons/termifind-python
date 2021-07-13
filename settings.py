import json
from pathlib import Path
from typing import Any


USER_SETTINGS_JSON_PATH: Path = Path("user_settings.json")


if USER_SETTINGS_JSON_PATH.exists():
    with open(USER_SETTINGS_JSON_PATH) as user_settings_json:
        USER_SETTINGS_DICTIONARY: dict[str, Any] = json.load(user_settings_json)
else:
    USER_SETTINGS_DICTIONARY = {}


def get_launch_path_setting() -> Path:
    launch_path_string: str = USER_SETTINGS_DICTIONARY.get("LAUNCH_PATH", None)

    if launch_path_string:
        launch_path: Path = Path(launch_path_string)
    else:
        launch_path = Path.home()

    return launch_path


class Settings:
    LAUNCH_PATH: Path = get_launch_path_setting()

    APPLICATION_SYMBOL: str = USER_SETTINGS_DICTIONARY.get("APPLICATION_SYMBOL", "App")
    DIRECTORY_SYMBOL: str = USER_SETTINGS_DICTIONARY.get("DIRECTORY_SYMBOL", "Dir")
    FILE_SYMBOL: str = USER_SETTINGS_DICTIONARY.get("FILE_SYMBOL", "Fil")
    SYMLINK_SYMBOL: str = USER_SETTINGS_DICTIONARY.get("SYMLINK_SYMBOL", "Sym")

    SHOULD_SHOW_DIRECTORY_ITEM_TYPE: bool = USER_SETTINGS_DICTIONARY.get("SHOULD_SHOW_DIRECTORY_ITEM_TYPE", True)
    SHOULD_SHOW_FILE_EXTENSIONS: bool = USER_SETTINGS_DICTIONARY.get("SHOULD_SHOW_FILE_EXTENSIONS", False)
    SHOULD_SHOW_HIDDEN_FILES: bool = USER_SETTINGS_DICTIONARY.get("SHOULD_SHOW_HIDDEN_FILES", False)
    SHOULD_SORT_CASE_SENSITIVE: bool = USER_SETTINGS_DICTIONARY.get("SHOULD_SORT_CASE_SENSITIVE", False)
