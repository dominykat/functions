class Boat:
    def __init__(self, model, color, value, ready_to_deploy):
        self.model = model
        self.color = color
        self.value = value
        self.ready_to_deploy = ready_to_deploy

    def description(self):
        return f"The {self.model} is a boat with color {self.color} worth ${self.value}. " \
               f"{'It is ready to deploy.' if self.ready_to_deploy else 'It is not ready to deploy.'}"


class CarWash:
    def __init__(self, wash_type, cost, payment_method):
        self.wash_type = wash_type
        self.cost = cost
        self.payment_method = payment_method

    def description(self):
        return f"The car wash is a {self.wash_type} wash with a cost of ${self.cost}. " \
               f"Accepts payment: {'Card' if self.payment_method == 'Card' else 'Cash'}."


class Restaurant:
    def __init__(self, starter, starter_cost, main, main_cost, dessert, dessert_cost):
        self.starter = starter
        self.starter_cost = starter_cost
        self.main = main
        self.main_cost = main_cost
        self.dessert = dessert
        self.dessert_cost = dessert_cost

    def total_cost(self):
        return self.starter_cost + self.main_cost + self.dessert_cost

    def description(self):
        return f"Starter: {self.starter} (${self.starter_cost}), " \
               f"Main: {self.main} (${self.main_cost}), " \
               f"Dessert: {self.dessert} (${self.dessert_cost}). " \
               f"Total Cost: ${self.total_cost()}"


# Creating instances of each class as a demonstration:

# Creating a boat instance
boat_example = Boat("Yacht", "White", 500000, True)

# Creating a car wash instance
car_wash_example = CarWash("Basic", 25, "Card")

# Creating a restaurant instance
restaurant_example = Restaurant("Salad", 10, "Steak", 30, "Ice Cream", 8)

# Now, let's print out descriptions to make sure everything is working as expected.
boat_description = boat_example.description()
car_wash_description = car_wash_example.description()
restaurant_description = restaurant_example.description()

boat_description, car_wash_description, restaurant_description
