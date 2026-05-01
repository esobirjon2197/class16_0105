
# 16-m
class Food:
    def __init__(self, name, calories, weight):
        self.name = name
        self.calories = calories
        self.weight = weight

    def prepare(self):
        print("Tayyorlanmoqda")


class FastFood(Food):
    def __init__(self, name, calories, weight, price, time):
        super().__init__(name, calories, weight)
        self.price = price
        self.time = time

    def prepare(self):
        super().prepare()
        print("Tez tayyor bo‘ladi")

    def serve(self):
        print(f"Narxi: {self.price}")


f = FastFood("Burger", 500, 200, 25000, "5 min")
f.prepare()
f.serve()
