class KeyboardHandler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, event):
        if self.successor:
            self.successor.handle(event)


class GameKeyboardHandler(KeyboardHandler):
    def __init__(self, game_app, ship, successor=None):
        super().__init__(successor)
        self.game_app = game_app
        self.ship = ship
