from libs.keyboard_event_handler.keyboard_event_handler import KeyboardHandler


class GameKeyboardHandler(KeyboardHandler):
    def __init__(self, game_app, ship, successor=None):
        super().__init__(successor)
        self.game_app = game_app
        self.ship = ship
