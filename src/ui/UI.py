from rich import print
from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.text import Text

from Settings import Settings
from src.PathContainer import PathContainer
from src.ui.LayoutRegion import LayoutRegion


class UI:
    def __init__(self) -> None:
        self.path_container: PathContainer = PathContainer(Settings.LAUNCH_PATH)
        # self.console: Console = Console()
        self.layout: Layout = Layout()

        path_panel: Panel = Panel(f"Current Path: {Settings.LAUNCH_PATH}", title="TermiFind", expand=True)

        layouts: list[Layout] = [
            Layout(path_panel, name=LayoutRegion.UPPER.name, size=3),
            Layout(name=LayoutRegion.LOWER.name),
        ]

        self.layout.split_column(*layouts)

        directory_container_panels: dict[str, Panel] = self.path_container.get_directory_container_panels_dictionary()

        default_panel: Panel = Panel(Text(""))

        previous_directory_container_panel: Panel = directory_container_panels.get(LayoutRegion.LEFT.name, default_panel)
        current_directory_container_panel: Panel = directory_container_panels.get(LayoutRegion.MIDDLE.name, default_panel)
        next_directory_container_panel: Panel = directory_container_panels.get(LayoutRegion.RIGHT.name, default_panel)

        if Settings.IS_IN_FOCUS_MODE:
            previous_directory_container_panel.style = Settings.FOCUS_MODE_DIMMED_STYLE
            next_directory_container_panel.style = Settings.FOCUS_MODE_DIMMED_STYLE

        layouts = [
            Layout(previous_directory_container_panel, name=LayoutRegion.LEFT.name),
            Layout(current_directory_container_panel, name=LayoutRegion.MIDDLE.name),
            Layout(next_directory_container_panel, name=LayoutRegion.RIGHT.name)
        ]

        self.layout[LayoutRegion.LOWER.name].split_row(*layouts)

    def start(self) -> None:
        with Live(self.layout, refresh_per_second=4, screen=True):
            Console().clear_live()
            print(self.layout)
            input("")
