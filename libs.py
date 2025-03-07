class Producer:
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location

    def __str__(self):
        return f"{self.name} located in {self.location}"

class Coffee:
    def __init__(self, taste: str, price):
        self.taste = taste
        self.price = price
        self.sold_out = False
        self.producer = Producer("Kopi", "Indonesia")

    def my_taste(self):
        print("Hello my taste is " + self.taste)

    def my_price(self):
        print("Hello my price is " + str(self.price))

    def set_sold_out(self):
        self.sold_out = True
        print(f"{self.taste} coffee has sold out")

    def check_sold_out(self):
        if self.sold_out:
            return f"{self.taste} coffee has sold out"
        else:
            return f"{self.taste} coffee is available"

    def set_producer(self, producer: Producer):
        self.producer = producer