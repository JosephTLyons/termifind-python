from rich import print
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel

from settings import Settings
from src.PathContainer import PathContainer
from src.UI.LayoutRegion import LayoutRegion


class UI:
    def __init__(self) -> None:
        self.path_container: PathContainer = PathContainer(Settings.LAUNCH_PATH)
        self.console: Console = Console()
        self.layout: Layout = Layout()

        self.top_panel: Panel = Panel(f"Current Path: {Settings.LAUNCH_PATH}", title="TermiFind", expand=True)

        self.layout.split_column(
            Layout(self.top_panel, name=str(LayoutRegion.UPPER), size=3),
            Layout(name=str(LayoutRegion.LOWER)),
        )

        self.bottom_panels: dict[LayoutRegion, Panel] = self.path_container.get_panels()

        self.layout[str(LayoutRegion.LOWER)].split_row(
            Layout(self.bottom_panels.get(LayoutRegion.LEFT, None), name=str(LayoutRegion.LEFT)),
            Layout(self.bottom_panels.get(LayoutRegion.MIDDLE, None), name=str(LayoutRegion.MIDDLE)),
            Layout(self.bottom_panels.get(LayoutRegion.RIGHT, None), name=str(LayoutRegion.RIGHT))
        )

    def print(self) -> None:
        with self.console.screen():
            print(self.layout)
            input("")
            # TODO: Fix
            self.console.clear()
