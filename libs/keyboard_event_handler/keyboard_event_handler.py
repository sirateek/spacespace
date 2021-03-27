class KeyboardHandler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, event):
        if self.successor:
            self.successor.handle(event)
