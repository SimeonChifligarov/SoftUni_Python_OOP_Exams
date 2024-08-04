from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, name: str, salary_one: float, salary_two: float, *children):
        super().__init__(name, budget=salary_one+salary_two, members_count=2+len(children))
        self.room_cost = 30
        self.children = list(children)
        self.appliances = [TV(), TV(), Fridge(), Fridge(), Laptop(), Laptop()]
        for _ in range(len(self.children)):

            # self.appliances.append(TV())
            # self.appliances.append(Fridge())
            # self.appliances.append(Laptop())

            self.appliances.extend([TV(), Fridge(), Laptop()])

        self.expenses = self.calculate_expenses(self.appliances, self.children)
