from libs.keyboard_event_handler.keyboard_event_handler import GameKeyboardHandler
from consts import BOMB_KEY


class BombKeyPressedHandler(GameKeyboardHandler):
    def handle(self, event):
        if event.char.upper() == BOMB_KEY:
            self.game_app.bomb.do_bomb()
        else:
            super().handle(event)
