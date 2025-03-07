from libs import Coffee
from libs import Producer

coffee_1 = Coffee("Sweet", 10000)
print(coffee_1.sold_out)
coffee_1.set_sold_out()
print(coffee_1.sold_out)

coffee_1.taste = "Bitter"
coffee_1.my_taste()
print(coffee_1.producer)
new_producer = Producer("Cappuccino", "Brazil")
coffee_1.set_producer(new_producer)
print(coffee_1.producer)