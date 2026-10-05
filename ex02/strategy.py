from abc import ABC, abstractmethod

from ex1.capability import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    """Exceção para uma combinação inválida entre estratégia e criatura."""


class ABattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature) -> str:
        pass


class NormalStrategy(ABattleStrategy):

    def is_valid(self, creature) -> bool:
        return True

    def act(self, creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                "NormalStrategy cannot be used with this Creature"
            )

        return creature.attack()


class AggressiveStrategy(ABattleStrategy):

    def is_valid(self, creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                "AggressiveStrategy cannot be used with this Creature"
            )

        actions = [
            creature.transform(),
            creature.attack(),
            creature.revert(),
        ]

        return "\n".join(actions)


class DefensiveStrategy(ABattleStrategy):

    def is_valid(self, creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                "DefensiveStrategy cannot be used with this Creature"
            )

        actions = [
            creature.attack(),
            creature.heal(),
        ]

        return "\n".join(actions)