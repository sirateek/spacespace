from consts import *
from libs.strategys.enemy_generation_strategy import EnemyGenerationStrategy
from utils import random_edge_position, normalize_vector
from elements import Enemy


class EdgeEnemyGenerationStrategy(EnemyGenerationStrategy):
    def generate(self, space_game, ship):
        x, y = random_edge_position()
        vx, vy = normalize_vector(ship.x - x, ship.y - y)

        vx *= ENEMY_BASE_SPEED
        vy *= ENEMY_BASE_SPEED

        enemy = Enemy(space_game, x, y, vx, vy)
        return [enemy]
