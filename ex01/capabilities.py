from abc import ABC, abstractmethod


class HealCapability(ABC):
    """Capacidade abstrata de cura."""

    @abstractmethod
    def heal(self, target=None) -> str:
        """Realiza uma ação de cura e retorna uma string descritiva."""
        pass


class TransformCapability(ABC):
    """Capacidade abstrata de transformação."""

    def __init__(self) -> None:
        self.transformed = False

    @abstractmethod
    def transform(self) -> str:
        """Transforma a criatura e retorna uma string descritiva."""
        pass

    @abstractmethod
    def revert(self) -> str:
        """Reverte a transformação e retorna uma string descritiva."""
        pass