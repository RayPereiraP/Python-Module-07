from ex0.creature import Creature

from .capability import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    """Criatura de Grama com capacidade de cura."""

    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self, target=None) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    """Criatura de Grama/Fada com capacidade de cura."""

    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance!"

    def heal(self, target=None) -> str:
        return f"{self.name} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    """Criatura Normal com capacidade de transformação."""

    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    """Criatura Normal/Dragão com capacidade de transformação."""

    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} stabilizes its form"