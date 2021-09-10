from rich.panel import Panel
from textual.reactive import Reactive  # type: ignore
from textual.widget import Widget  # type: ignore
from textual.widgets import Button  # type: ignore


class TermiFindButton(Button):  # type: ignore
    ...


class TermiFindPanelWidget(Widget):  # type: ignore
    mouse_over = Reactive(False)

    def __init__(self, panel: Panel) -> None:
        super().__init__()
        self.panel: Panel = panel

    def render(self) -> Panel:
        return self.panel
