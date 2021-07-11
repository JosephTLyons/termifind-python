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

        upper_panel: Panel = Panel(f"Current Path: {Settings.LAUNCH_PATH}", title="TermiFind", expand=True)

        self.layout.split_column(
            Layout(upper_panel, name=LayoutRegion.UPPER.name, size=3),
            Layout(name=LayoutRegion.LOWER.name),
        )

        lower_panels: dict[LayoutRegion, Panel] = self.path_container.get_panels()
        lower_left_panel = lower_panels.get(LayoutRegion.LEFT.name, None)
        lower_middle_panel = lower_panels.get(LayoutRegion.MIDDLE.name, None)
        lower_right_panel = lower_panels.get(LayoutRegion.RIGHT.name, None)

        self.layout[str(LayoutRegion.LOWER)].split_row(
            Layout(lower_left_panel, name=LayoutRegion.LEFT.name),
            Layout(lower_middle_panel, name=LayoutRegion.MIDDLE.name),
            Layout(lower_right_panel, name=LayoutRegion.RIGHT.name)
        )

    def print(self) -> None:
        with self.console.screen():
            print(self.layout)
            input("")
            # TODO: Fix
            self.console.clear()
