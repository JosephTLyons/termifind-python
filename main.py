from textual.app import App  # type: ignore

from src.ui.ui import UI


class TermiFindApplication(App):  # type: ignore
    def __init__(self, *args, **kwargs):  # type: ignore
        super().__init__(*args, **kwargs)
        self.ui: UI = UI()

    async def on_load(self) -> None:
        await self.bind("q", "quit")

    async def on_mount(self) -> None:
        await self.view.dock(self.ui.termifind_panel_widget, edge="top", size=3)
        await self.view.dock(
            self.ui.previous_directory_container_panel_widget,
            self.ui.current_directory_container_panel_widget,
            self.ui.next_directory_container_panel_widget,
            edge="left"
        )


def main() -> None:
    TermiFindApplication.run(log="termifind.log")


if __name__ == "__main__":
    main()
