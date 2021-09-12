from textual.layouts.vertical import VerticalLayout
from textual.view import View
from textual.widgets import ScrollView

from src.ui.custom_widgets import TermiFindButton


class TermiFindButtonsView(View, layout=VerticalLayout):  # type: ignore
    def add(self, button: TermiFindButton) -> None:
        self.layout.add(button)

class TermiFindScrollView(ScrollView):  # type: ignore
    async def key_down(self) -> None:
        self.target_y += 1
        self.animate("y", self.target_y, easing="linear", speed=100)

    async def key_up(self) -> None:
        self.target_y -= 1
        self.animate("y", self.target_y, easing="linear", speed=100)
