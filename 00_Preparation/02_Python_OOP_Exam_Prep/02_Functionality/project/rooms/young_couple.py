from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, name: str, salary_one: float, salary_two: float):
        super().__init__(name, budget=salary_one+salary_two, members_count=2)
        self.room_cost = 20
        self.appliances = [TV(), TV(), Fridge(), Fridge(), Laptop(), Laptop()]
        self.expenses = self.calculate_expenses(self.appliances)
