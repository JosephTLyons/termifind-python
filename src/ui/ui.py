from typing import Optional

from rich import print
from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.text import Text

from Settings import Settings
from src.directory_container import DirectoryContainer
from src.path_container import PathContainer
from src.directory_item.directory_item_type import get_directory_item_type_attributes
from src.ui.layout_region import LayoutRegion


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

        should_style_text: bool = not Settings.IS_IN_FOCUS_MODE

        previous_directory_container_panel: Panel = self.get_directory_container_panel(
            self.path_container.previous_directory_container, should_style_text
        )
        current_directory_container_panel: Panel = self.get_directory_container_panel(
            self.path_container.current_directory_container
        )
        next_directory_container_panel: Panel = self.get_directory_container_panel(
            self.path_container.next_directory_container, should_style_text
        )

        if Settings.IS_IN_FOCUS_MODE:
            previous_directory_container_panel.style = Settings.FOCUS_MODE_DIMMED_STYLE
            next_directory_container_panel.style = Settings.FOCUS_MODE_DIMMED_STYLE

        layouts = [
            Layout(previous_directory_container_panel, name=LayoutRegion.LEFT.name),
            Layout(current_directory_container_panel, name=LayoutRegion.MIDDLE.name),
            Layout(next_directory_container_panel, name=LayoutRegion.RIGHT.name)
        ]

        self.layout[LayoutRegion.LOWER.name].split_row(*layouts)

    # Maybe move this out of the UI class an into main() or some Console class?
    def start(self) -> None:
        with Live(self.layout, refresh_per_second=4, screen=True):
            Console().clear_live()
            user_input = ""

            while user_input.lower() != "q":
                print(self.layout)
                user_input = input("")

    def get_directory_container_panel(self, directory_container: Optional[DirectoryContainer], should_style_text: bool = True) -> Panel:
        if not directory_container:
            return Panel(Text(""))

        item_name_texts: Text = self.__get_item_name_text(directory_container, should_style_text)

        return Panel(item_name_texts, title=str(directory_container), expand=True)

    def __get_item_name_text(self, directory_container: DirectoryContainer, should_style_text: bool) -> Text:
        item_name_text: Text = Text(no_wrap=True, overflow="ellipsis")

        for index, directory_item in enumerate(directory_container.directory_items):
            if index == directory_container.selected_item_index:
                selection_status: str = Settings.SELECTOR_SYMBOL
            else:
                selection_status = " " * len(Settings.SELECTOR_SYMBOL)

            if should_style_text:
                select_symbol_style: Optional[str] = Settings.SELECTOR_SYMBOL_STYLE
                directory_item_type_style: Optional[str] = get_directory_item_type_attributes(directory_item.directory_item_type).style
            else:
                select_symbol_style = None
                directory_item_type_style = None

            item_name_text.append(f"{selection_status} ", style=select_symbol_style)
            item_name_text.append(f"{directory_item}\n", style=directory_item_type_style)

        return item_name_text
