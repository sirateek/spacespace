from libs.keyboard_event_handler.keyboard_event_handler import GameKeyboardHandler
from consts import LEFT_KEY, RIGHT_KEY, BOMB_KEY, FIRE_KEY


class ShipMovementKeyPressedHandler(GameKeyboardHandler):
    def handle(self, event):
        if event.keysym == LEFT_KEY:
            self.ship.start_turn('LEFT')
        elif event.keysym == RIGHT_KEY:
            self.ship.start_turn('RIGHT')
        elif event.char == FIRE_KEY:
            self.ship.fire()
        elif event.char.upper() == BOMB_KEY:
            self.bomb()


class ShipMovementKeyReleasedHandler(GameKeyboardHandler):
    def handle(self, event):
        if event.keysym == LEFT_KEY:
            self.ship.stop_turn('LEFT')
        elif event.keysym == RIGHT_KEY:
            self.ship.stop_turn('RIGHT')
