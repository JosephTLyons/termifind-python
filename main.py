from textual.app import App  # type: ignore

from settings import Settings
from src.path_container import PathContainer
from src.ui.ui import UI


class TermiFindApplication(App):  # type: ignore
    def __init__(self, *args, **kwargs):  # type: ignore
        super().__init__(*args, **kwargs)

        # Separation of main data structure and ui
        self.path_container: PathContainer = PathContainer(Settings.LAUNCH_PATH)
        self.ui: UI = UI(self.path_container)

    async def on_load(self) -> None:
        await self.bind("q", "quit")

    async def on_mount(self) -> None:
        await self.view.dock(self.ui.termifind_panel_widget, edge="top", size=3)
        await self.view.dock(
            self.ui.previous_directory_container_scroll_view,
            self.ui.current_directory_container_scroll_view,
            self.ui.next_directory_container_scroll_view,
            edge="left"
        )


def main() -> None:
    TermiFindApplication.run(log="termifind.log")


if __name__ == "__main__":
    main()
