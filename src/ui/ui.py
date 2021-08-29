from src.directory_item.directory_item import DirectoryItemMetaData
from typing import Optional

from rich.panel import Panel
from rich.text import Text
from textual.reactive import Reactive  # type: ignore
from textual.widget import Widget  # type: ignore


from settings import Settings
from src.directory_container import DirectoryContainer
from src.path_container import PathContainer
from src.directory_item.directory_item_type import get_directory_item_type_attributes

class TermiFindPanelWidget(Widget):  # type: ignore
    mouse_over = Reactive(False)

    def __init__(self, panel: Panel) -> None:
        super().__init__()
        self.panel: Panel = panel

    def render(self) -> Panel:
        return self.panel


class UI:
    def __init__(self) -> None:
        path_panel: Panel = Panel(f"Current Path: {Settings.LAUNCH_PATH}", title="TermiFind", expand=True)
        self.termifind_panel_widget: TermiFindPanelWidget = TermiFindPanelWidget(path_panel)

        path_container: PathContainer = PathContainer(Settings.LAUNCH_PATH)

        should_style_text: bool = not Settings.IS_IN_FOCUS_MODE

        previous_directory_container_panel: Panel = self.__get_main_panel(
            path_container.previous_directory_container, should_style_text
        )
        current_directory_container_panel: Panel = self.__get_main_panel(
            path_container.current_directory_container
        )
        next_directory_container_panel: Panel = self.__get_main_panel(
            path_container.selected_item_contents_preview, should_style_text
        )

        if Settings.IS_IN_FOCUS_MODE:
            previous_directory_container_panel.style = Settings.FOCUS_MODE_DIMMED_STYLE
            next_directory_container_panel.style = Settings.FOCUS_MODE_DIMMED_STYLE

        self.previous_directory_container_panel_widget: TermiFindPanelWidget = TermiFindPanelWidget(
            previous_directory_container_panel
        )
        self.current_directory_container_panel_widget: TermiFindPanelWidget = TermiFindPanelWidget(
            current_directory_container_panel
        )
        self.next_directory_container_panel_widget: TermiFindPanelWidget = TermiFindPanelWidget(
            next_directory_container_panel
        )

    def __get_main_panel(self, directory_container: Optional[DirectoryContainer | DirectoryItemMetaData], should_style_text: bool = True) -> Panel:
        if not directory_container:
            return Panel(Text(""))

        # TODO: Use a better system to replace using isinstance, which is gross
        if isinstance(directory_container, DirectoryContainer):
            item_name_text: Text = self.__get_directory_container_item_name_text(directory_container, should_style_text)
        else:
            item_name_text = self.__get_metadata_item_name_text(directory_container, should_style_text)

        return Panel(item_name_text, title=str(directory_container), expand=True)

    def __get_directory_container_item_name_text(self, directory_container: DirectoryContainer, should_style_text: bool) -> Text:
        item_name_text: Text = Text(no_wrap=True, overflow="ellipsis")

        for index, directory_item in enumerate(directory_container.directory_items):
            if index == directory_container.selected_item_index and directory_container.selected_item:
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

    def __get_metadata_item_name_text(self, directory_item_metadata: DirectoryItemMetaData, should_style_text: bool) -> Text:
        item_name_text: Text = Text(no_wrap=True, overflow="ellipsis")

        file_metadata_dictionary = directory_item_metadata.get_file_metadata_dictionary()
        length_of_longest_metadata_name = len(max(file_metadata_dictionary.keys(), key=len))

        for metadata_name, metadata_value in file_metadata_dictionary.items():
            padded_metadata_name = (metadata_name).ljust(length_of_longest_metadata_name)
            item_name_text.append(f"* {padded_metadata_name} | {metadata_value}\n")

        return item_name_text
