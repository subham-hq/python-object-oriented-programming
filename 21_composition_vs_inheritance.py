"""
Composition vs Inheritance
==========================

- Inheritance models "IS-A" (a Developer IS-A Employee).
- Composition models "HAS-A" (a Car HAS-AN Engine). The object holds other
  objects and delegates work to them.

Favour composition when there is no clean IS-A relationship: it is more
flexible, avoids deep/fragile hierarchies, and lets you swap parts at runtime.

Key idea:
    Reach for inheritance only for a genuine IS-A. For "made up of" or "uses-a",
    compose objects and delegate.
"""


class Engine:
    def __init__(self, horsepower: int) -> None:
        self.horsepower = horsepower

    def start(self) -> str:
        return f"engine ({self.horsepower}hp) running"


class GPS:
    def route(self, dest: str) -> str:
        return f"routing to {dest}"


class Car:
    # Car HAS-AN Engine and HAS-A GPS (composition), rather than inheriting.
    def __init__(self, model: str, horsepower: int) -> None:
        self.model = model
        self.engine = Engine(horsepower)   # owned component
        self.gps = GPS()

    def start(self) -> str:
        return f"{self.model}: {self.engine.start()}"   # delegate to component

    def navigate(self, dest: str) -> str:
        return self.gps.route(dest)


if __name__ == "__main__":
    car = Car("Model-X", 350)
    print(car.start())              # delegates to Engine
    print(car.navigate("Asansol"))  # delegates to GPS

    # You can swap a component at runtime -- flexibility composition gives you:
    car.engine = Engine(500)
    print(car.start())

    # Expected output:
    #   Model-X: engine (350hp) running
    #   routing to Asansol
    #   Model-X: engine (500hp) running
