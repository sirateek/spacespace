from gamelib import Text


class StatusWithText:
    def __init__(self, app, x, y, text_template, default_value=0):
        self.x = x
        self.y = y
        self.text_template = text_template
        self._value = default_value
        self.label_text = Text(app, '', x, y)
        self.update_label()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v
        self.update_label()

    def update_label(self):
        self.label_text.set_text(self.text_template % self.value)
