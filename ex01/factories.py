from ex0.factory import CreatureFactory

from .creature import (
    Sproutling,
    Bloomelle,
    Shiftling,
    Morphagon,
)


class HealingCreatureFactory(CreatureFactory):
    """Fábrica para a família de criaturas com capacidade de cura."""

    def create_base(self):
        return Sproutling()

    def create_evolved(self):
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    """Fábrica para a família de criaturas com capacidade de transformação."""

    def create_base(self):
        return Shiftling()

    def create_evolved(self):
        return Morphagon()
