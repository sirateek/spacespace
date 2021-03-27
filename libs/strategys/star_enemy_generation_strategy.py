from libs.strategys.enemy_generation_strategy import EnemyGenerationStrategy
from consts import *
from random import randint
from utils import normalize_vector, vector_len, direction_to_dxdy
from elements import Enemy


class StarEnemyGenerationStrategy(EnemyGenerationStrategy):
    def generate(self, space_game, ship):
        enemies = []

        x = randint(100, CANVAS_WIDTH - 100)
        y = randint(100, CANVAS_HEIGHT - 100)

        while vector_len(x - ship.x, y - ship.y) < 200:
            x = randint(100, CANVAS_WIDTH - 100)
            y = randint(100, CANVAS_HEIGHT - 100)

        for d in range(18):
            dx, dy = direction_to_dxdy(d * 20)
            enemy = Enemy(space_game, x, y, dx * ENEMY_BASE_SPEED,
                          dy * ENEMY_BASE_SPEED)
            enemies.append(enemy)

        return enemies
