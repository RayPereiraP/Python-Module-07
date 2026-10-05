from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
)


def battle(opponents):
    creatures = []

    for factory, strategy in opponents:
        creature = factory.create_base()

        if not strategy.is_valid(creature):
            try:
                strategy.act(creature)
            except InvalidStrategyError as error:
                print(error)
            continue

        creatures.append((creature, strategy))

    for i in range(len(creatures)):
        for j in range(i + 1, len(creatures)):
            creature1, strategy1 = creatures[i]
            creature2, strategy2 = creatures[j]

            print(f"{creature1.name} vs {creature2.name}")

            print(strategy1.act(creature1))
            print(strategy2.act(creature2))


if __name__ == "__main__":
    opponents = [
        (FlameFactory(), NormalStrategy()),
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ]

    battle(opponents)