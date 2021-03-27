from abc import ABC, abstractmethod


class EnemyGenerationStrategy(ABC):
    @abstractmethod
    def generate(self, space_game, ship):
        pass
