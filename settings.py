import json
from pathlib import Path

with open("user_settings.json") as user_settings_json:
    USER_SETTINGS_DICTIONARY = json.load(user_settings_json)


def get_launch_path_setting() -> Path:
    launch_path_string: str = USER_SETTINGS_DICTIONARY.get("LAUNCH_PATH", None)

    if launch_path_string:
        launch_path: Path = Path(launch_path_string)
    else:
        launch_path = Path.home()

    return launch_path


class Settings:
    LAUNCH_PATH: Path = get_launch_path_setting()

    SHOULD_SHOW_FILE_EXTENSIONS: bool = USER_SETTINGS_DICTIONARY.get("SHOULD_SHOW_FILE_EXTENSIONS", False)
    SHOULD_SHOW_HIDDEN_FILES: bool = USER_SETTINGS_DICTIONARY.get("SHOULD_SHOW_HIDDEN_FILES", False)
    SHOULD_SORT_CASE_SENSITIVE: bool = USER_SETTINGS_DICTIONARY.get("SHOULD_SORT_CASE_SENSITIVE", False)

    APPLICATION_SYMBOL: str = USER_SETTINGS_DICTIONARY.get("APPLICATION_SYMBOL", "A")
    DIRECTORY_SYMBOL: str = USER_SETTINGS_DICTIONARY.get("DIRECTORY_SYMBOL", "D")
    FILE_SYMBOL: str = USER_SETTINGS_DICTIONARY.get("FILE_SYMBOL", "F")
    SYMLINK_SYMBOL: str = USER_SETTINGS_DICTIONARY.get("SYMLINK_SYMBOL", "S")
