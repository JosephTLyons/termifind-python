from typing import Optional

from rich.panel import Panel
from rich.text import Text

from settings import Settings
from src.directory_container import DirectoryContainer
from src.directory_item.directory_item import DirectoryItemMetaData
from src.directory_item.directory_item_type import get_directory_item_type_attributes
from src.ui.custom_views import TermiFindButtonsView, TermiFindScrollView
from src.ui.custom_widgets import TermiFindButton, TermiFindPanelWidget
from src.path_container import PathContainer


class UI:
    def __init__(self, path_container: PathContainer) -> None:
        path_panel: Panel = Panel(f"Current Path: {Settings.LAUNCH_PATH}", title="TermiFind", expand=True)
        self.termifind_path_panel_widget: TermiFindPanelWidget = TermiFindPanelWidget(path_panel)

        should_style_text: bool = not Settings.IS_IN_FOCUS_MODE

        self.previous_directory_container_scroll_view: TermiFindScrollView = self.__get_scroll_view(
            path_container.previous_directory_container, should_style_text
        )
        self.current_directory_container_scroll_view: TermiFindScrollView = self.__get_scroll_view(
            path_container.current_directory_container
        )
        self.next_directory_container_scroll_view: TermiFindScrollView = self.__get_scroll_view(
            path_container.selected_item_contents_preview, should_style_text
        )

    def __get_scroll_view(self, directory_container: Optional[DirectoryContainer | DirectoryItemMetaData], should_style_text: bool = True) -> TermiFindScrollView:
        if not directory_container:
            return TermiFindScrollView()

        # TODO: Use a better system to replace using `isinstance`, which is gross
        if isinstance(directory_container, DirectoryContainer):
            item_buttons_view: TermiFindButtonsView = self.__get_item_buttons_view(directory_container, should_style_text)
            scroll_view = TermiFindScrollView(item_buttons_view)
        else:
            meta_data_text: Text = self.__get_item_metadata_text(directory_container)
            scroll_view = TermiFindScrollView(meta_data_text)

        return scroll_view

    def __get_item_buttons_view(self, directory_container: DirectoryContainer, should_style_text: bool) -> TermiFindButtonsView:
        termifind_buttons_view: TermiFindButtonsView = TermiFindButtonsView()

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

            item_name_text: Text = Text(no_wrap=True, overflow="ellipsis")
            item_name_text.append(f"{selection_status} ", style=select_symbol_style)
            item_name_text.append(f"{directory_item}", style=directory_item_type_style)

            termifind_buttons_view.add(TermiFindButton(item_name_text))

        # TODO: Delete
        for widget in termifind_buttons_view.layout.get_widgets():
            print(widget)

        print()

        return termifind_buttons_view

    def __get_item_metadata_text(self, directory_item_metadata: DirectoryItemMetaData) -> Text:
        item_name_text: Text = Text(no_wrap=True, overflow="ellipsis")

        file_metadata_dictionary = directory_item_metadata.get_file_metadata_dictionary()
        length_of_longest_metadata_name = len(max(file_metadata_dictionary.keys(), key=len))

        for metadata_name, metadata_value in file_metadata_dictionary.items():
            padded_metadata_name = (metadata_name).ljust(length_of_longest_metadata_name)
            item_name_text.append(f"* {padded_metadata_name} | {metadata_value}\n")

        return item_name_text
