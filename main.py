import math
from random import randint, random

import tkinter as tk

from gamelib import Sprite, GameApp, Text, KeyboardHandler

from consts import *
from elements import Ship, Bullet, Enemy
from utils import distance
from libs.strategys.importer import StarEnemyGenerationStrategy, EdgeEnemyGenerationStrategy
from libs.keyboard_event_handler.importer import ShipMovementKeyPressedHandler, ShipMovementKeyReleasedHandler, BombKeyPressedHandler
from libs.status_display.status_with_text import StatusWithText


class SpaceGame(GameApp):
    def init_game(self):
        self.ship = Ship(self, CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)

        self.level = 1
        self.level_text = Text(self, '', 100, 580)
        self.update_level_text()

        self.score_wait = 0
        self.score = StatusWithText(self, 100, 20, 'Score: %d', 0)

        self.bomb_power = StatusWithText(
            self, 700, 20, "Power: %d", BOMB_FULL_POWER)
        self.bomb_wait = 0

        self.elements.append(self.ship)

        self.enemy_creation_strategies = [
            (0.2, StarEnemyGenerationStrategy()),
            (1.0, EdgeEnemyGenerationStrategy())
        ]

        self.enemies = []
        self.bullets = []
        self.init_key_handlers()

    def init_key_handlers(self):
        key_pressed_handler = ShipMovementKeyPressedHandler(self, self.ship)
        key_pressed_handler = BombKeyPressedHandler(
            self, self.ship, key_pressed_handler)
        self.key_pressed_handler = key_pressed_handler

        key_released_handler = ShipMovementKeyReleasedHandler(self, self.ship)
        self.key_released_handler = key_released_handler

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def add_bullet(self, bullet):
        self.bullets.append(bullet)

    def bullet_count(self):
        return len(self.bullets)

    def bomb(self):
        if self.bomb_power.value == BOMB_FULL_POWER:
            self.bomb_power.value = 0

            self.bomb_canvas_id = self.canvas.create_oval(
                self.ship.x - BOMB_RADIUS,
                self.ship.y - BOMB_RADIUS,
                self.ship.x + BOMB_RADIUS,
                self.ship.y + BOMB_RADIUS
            )

            self.after(200, lambda: self.canvas.delete(self.bomb_canvas_id))

            for e in self.enemies:
                if self.ship.distance_to(e) <= BOMB_RADIUS:
                    e.to_be_deleted = True

    def update_level_text(self):
        self.level_text.set_text('Level: %d' % self.level)

    def update_score(self):
        self.score_wait += 1
        if self.score_wait >= SCORE_WAIT:
            self.score.value += 1
            self.score_wait = 0

    def update_bomb_power(self):
        self.bomb_wait += 1
        if (self.bomb_wait >= BOMB_WAIT) and (self.bomb_power.value != BOMB_FULL_POWER):
            self.bomb_power.value += 1
            self.bomb_wait = 0

    def create_enemies(self):
        p = random()

        for prob, strategy in self.enemy_creation_strategies:
            if p < prob:
                enemies = strategy.generate(self, self.ship)
                break

        for e in enemies:
            self.add_enemy(e)

    def pre_update(self):
        if random() < 0.1:
            self.create_enemies()

    def process_bullet_enemy_collisions(self):
        for b in self.bullets:
            for e in self.enemies:
                if b.is_colliding_with_enemy(e):
                    b.to_be_deleted = True
                    e.to_be_deleted = True

    def process_ship_enemy_collision(self):
        if IS_DEATHABLE:
            for e in self.enemies:
                if self.ship.is_colliding_with_enemy(e):
                    self.stop_animation()

    def process_collisions(self):
        self.process_bullet_enemy_collisions()
        self.process_ship_enemy_collision()

    def update_and_filter_deleted(self, elements):
        new_list = []
        for e in elements:
            e.update()
            e.render()
            if e.to_be_deleted:
                e.delete()
            else:
                new_list.append(e)
        return new_list

    def post_update(self):
        self.process_collisions()

        self.bullets = self.update_and_filter_deleted(self.bullets)
        self.enemies = self.update_and_filter_deleted(self.enemies)

        self.update_score()
        self.update_bomb_power()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Space Fighter")

    # do not allow window resizing
    root.resizable(False, False)
    app = SpaceGame(root, CANVAS_WIDTH, CANVAS_HEIGHT, UPDATE_DELAY)
    app.start()
    root.mainloop()
