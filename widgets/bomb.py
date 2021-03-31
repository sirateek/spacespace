import tkinter as tk
from widgets.importer import StatusWithText, ProgressBar
from consts import BOMB_FULL_POWER, BOMB_WAIT, BOMB_RADIUS


class Bomb:
    def __init__(self, app, ship, bomb_image="images/bomb.png"):
        self.app = app
        self.ship = ship
        self.bomb_power_bar = ProgressBar(
            self.app, length=100, init_progress_value=100)
        self.bomb_image = tk.PhotoImage(file=bomb_image)
        self.app.canvas.create_image(
            610, 0, image=self.bomb_image, anchor="nw")
        self.app.canvas.create_window(700, 20, window=self.bomb_power_bar)
        self.bomb_wait = 0
        self.bomb_destraction_area = BombDestructionArea(self.app)

    def update_bomb_power(self):
        self.bomb_wait += 1
        if (self.bomb_wait >= BOMB_WAIT) and (self.bomb_power_bar.value != BOMB_FULL_POWER):
            self.bomb_power_bar.value += 1
            self.bomb_wait = 0

    def do_bomb(self):
        if self.bomb_power_bar.value == BOMB_FULL_POWER:
            self.bomb_power_bar.change_progress_value(0, time_interval=2)
            self.bomb_destraction_area.create_destruction_area(
                (self.ship.x, self.ship.y), BOMB_RADIUS, self.animate_callback_handler)

    def animate_callback_handler(self, radius):
        for e in self.app.enemies:
            if self.ship.distance_to(e) <= radius:
                e.to_be_deleted = True


class BombDestructionArea:
    def __init__(self, app):
        self.app = app
        self.center_at = (None, None)
        self.current_radius = 0
        self.bomb_destruction_area = None

    def create_destruction_area(self, center_at, radius, animate_callback):
        assert type(center_at) == tuple, "The center_at must be a tuple"
        self.center_at = center_at
        self.animate_area(radius, animate_callback)

    def animate_area(self, radius, animate_callback, time_interval=1):
        assert callable(
            animate_callback), "The animate_callback must be a call back function"
        assert radius != 0, "The radius can't be zero"
        if self.current_radius == radius:
            self.current_radius = 0
            self.app.canvas.delete(
                self.bomb_destruction_area)
            self.bomb_destruction_area = None
            return
        self.current_radius += 1
        self.app.canvas.delete(self.bomb_destruction_area)
        self.bomb_destruction_area = self.app.canvas.create_oval(
            self.center_at[0] - self.current_radius,
            self.center_at[1] - self.current_radius,
            self.center_at[0] + self.current_radius,
            self.center_at[1] + self.current_radius,
        )
        animate_callback(self.current_radius)
        self.app.after(time_interval, lambda: self.animate_area(
            radius, animate_callback, time_interval))
