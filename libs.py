class Barista:
    def __init__(self, name: str, experience_level: str):
        self.name = name
        self.experience_level = experience_level

    def __str__(self):
        return f"{self.name}, {self.experience_level} barista"


class Coffee:
    def __init__(
        self,
        name: str,
        price: float,
        available=True,
        barista=Barista("Unknown", "Novice"),
    ):
        self.name = name
        self.price = price
        self.available = available
        self.barista = barista

    def coffee_info(self):
        print(f"Coffee: {self.name}, Price: {self.price}, Barista: {self.barista}")

    def set_unavailable(self):
        self.available = False
        print(f"{self.name} is now unavailable")

    def check_availability(self):
        if self.available:
            return f"{self.name} is available"
        else:
            return f"{self.name} is unavailable"

    def set_barista(self, barista: Barista):
        self.barista = barista
