from pathlib import Path


class DefaultSettings:
    LAUNCH_PATH: Path = Path.home()
    SHOULD_SHOW_HIDDEN_FILES: bool = False
    SHOULD_SORT_CASE_SENSITIVE: bool = False


class Settings(DefaultSettings):
    """A place to override the default settings"""
    pass
