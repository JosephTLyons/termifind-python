from rich.console import Console

from settings import Settings
from src.PathContainer import PathContainer


def main() -> None:
    console: Console = Console()

    with console.screen():
        path_container: PathContainer = PathContainer(Settings.LAUNCH_PATH)
        path_container.print()
        input("")
        # TODO: Fix
        console.clear()


if __name__ == "__main__":
    main()
