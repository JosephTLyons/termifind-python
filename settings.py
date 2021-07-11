from pathlib import Path


class DefaultSettings:
    LAUNCH_PATH: Path = Path.home()
    SHOULD_SHOW_HIDDEN_FILES: bool = False
    SHOULD_SORT_CASE_SENSITIVE: bool = False
    DIRECTORY_SYMBOL: str = "D"
    FILE_SYMBOL: str = "F"
    SYMLINK_SYMBOL: str = "S"


class Settings(DefaultSettings):
    """A place to override the default settings"""
    LAUNCH_PATH: Path = Path("/")
    DIRECTORY_SYMBOL: str = "Dir"
    FILE_SYMBOL: str = "Fil"
    SYMLINK_SYMBOL: str = "Sym"
