class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = self.calculate_expenses(self.children)

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")

        self.__expenses = value

    @staticmethod
    def calculate_expenses(*args):
        total_expenses = 0
        for el_as_list in args:
            for obj in el_as_list:
                total_expenses += obj.get_monthly_expense()

        return total_expenses
