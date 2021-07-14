import json
from pathlib import Path
from typing import Any, Optional


USER_SETTINGS_JSON_PATH: Path = Path("user_settings.json")


if USER_SETTINGS_JSON_PATH.exists():
    with open(USER_SETTINGS_JSON_PATH) as user_settings_json:
        USER_SETTINGS_DICTIONARY: dict[str, Any] = json.load(user_settings_json)
else:
    USER_SETTINGS_DICTIONARY = {}


def get_launch_path_setting() -> Path:
    launch_path_string: Optional[str] = USER_SETTINGS_DICTIONARY.get("LAUNCH_PATH", None)
    launch_path: Path = Path.home()

    if launch_path_string:
        try:
            launch_path = Path(launch_path_string)
        except FileNotFoundError:
            pass

    return launch_path


class Settings:
    LAUNCH_PATH: Path = get_launch_path_setting()

    APPLICATION_SYMBOL: str = USER_SETTINGS_DICTIONARY.get("APPLICATION_SYMBOL", "App")
    DIRECTORY_SYMBOL: str = USER_SETTINGS_DICTIONARY.get("DIRECTORY_SYMBOL", "Dir")
    FILE_SYMBOL: str = USER_SETTINGS_DICTIONARY.get("FILE_SYMBOL", "Fil")
    SYMLINK_SYMBOL: str = USER_SETTINGS_DICTIONARY.get("SYMLINK_SYMBOL", "Sym")

    APPLICATION_STYLE: str = USER_SETTINGS_DICTIONARY.get("APPLICATION_STYLE", "bright_white")
    DIRECTORY_STYLE: str = USER_SETTINGS_DICTIONARY.get("DIRECTORY_STYLE", "bold green")
    FILE_STYLE: str = USER_SETTINGS_DICTIONARY.get("FILE_STYLE", "bright_white")
    SYMLINK_STYLE: str = USER_SETTINGS_DICTIONARY.get("SYMLINK_STYLE", "bright_white")

    IS_IN_FOCUS_MODE: bool = USER_SETTINGS_DICTIONARY.get("IS_IN_FOCUS_MODE", False)
    FOCUS_MODE_DIMMED_STYLE: str = USER_SETTINGS_DICTIONARY.get("FOCUS_MODE_DIMMED_STYLE", "grey58")

    SHOULD_SHOW_DIRECTORY_ITEM_TYPE: bool = USER_SETTINGS_DICTIONARY.get("SHOULD_SHOW_DIRECTORY_ITEM_TYPE", True)
    SHOULD_SHOW_FILE_EXTENSIONS: bool = USER_SETTINGS_DICTIONARY.get("SHOULD_SHOW_FILE_EXTENSIONS", False)
    SHOULD_SHOW_HIDDEN_FILES: bool = USER_SETTINGS_DICTIONARY.get("SHOULD_SHOW_HIDDEN_FILES", False)
    SHOULD_SORT_CASE_SENSITIVE: bool = USER_SETTINGS_DICTIONARY.get("SHOULD_SORT_CASE_SENSITIVE", False)
