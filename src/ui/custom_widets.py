from rich.panel import Panel
from textual.layouts.vertical import VerticalLayout  # type: ignore
from textual.reactive import Reactive  # type: ignore
from textual.view import View
from textual.widget import Widget  # type: ignore
from textual.widgets import Button, ScrollView  # type: ignore


class TermiFindButtonsView(View, layout=VerticalLayout):
    def add(self, button):
        self.layout.add(button)


class TermiFindButton(Button):
    ...


class TermiFindPanel(Widget):  # type: ignore
    mouse_over = Reactive(False)

    def __init__(self, panel: Panel) -> None:
        super().__init__()
        self.panel: Panel = panel

    def render(self) -> Panel:
        return self.panel


class TermiFindScrollView(ScrollView):
    async def key_down(self) -> None:
        self.target_y += 1
        self.animate("y", self.target_y, easing="linear", speed=100)

    async def key_up(self) -> None:
        self.target_y -= 1
        self.animate("y", self.target_y, easing="linear", speed=100)
