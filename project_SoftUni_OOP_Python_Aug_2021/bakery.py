from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value.isspace():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):

        for f in self.food_menu:
            if f.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")

        current_food = None
        if food_type == "Bread":
            current_food = Bread(name, price)
            self.food_menu.append(current_food)
            return f"Added {name} (Bread) to the food menu"
        if food_type == "Cake":
            current_food = Cake(name, price)
            self.food_menu.append(current_food)
            return f"Added {name} (Cake) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):

        for d in self.drinks_menu:
            if d.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")

        current_drink = None
        if drink_type == "Tea":
            current_drink = Tea(name, portion, brand)
            self.drinks_menu.append(current_drink)
            return f"Added {current_drink.name} ({current_drink.brand}) to the drink menu"
        if drink_type == "Water":
            current_drink = Water(name, portion, brand)
            self.drinks_menu.append(current_drink)
            return f"Added {current_drink.name} ({current_drink.brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):

        for t in self.tables_repository:
            if t.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

        current_table = None
        if table_type == "InsideTable":
            current_table = InsideTable(table_number, capacity)
            self.tables_repository.append(current_table)
            return f"Added table number {table_number} in the bakery"
        if table_type == "OutsideTable":
            current_table = OutsideTable(table_number, capacity)
            self.tables_repository.append(current_table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        
        # ordered_tables = sorted(self.tables_repository, key=lambda x: x.table_number)

        for t in self.tables_repository:
            if not t.is_reserved and t.number_of_people == 0 and t.capacity >= number_of_people:
                t.is_reserved = True
                t.number_of_people = number_of_people
                return f"Table {t.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):

        # if table_number not in [t.table_number for t in self.tables_repository]:
        #     return f"Could not find table {table_number}"
        #
        # current_table = [t for t in self.tables_repository if t.table_number == table_number][0]
        #
        # possible_foods = list(food_names)
        #
        # real_orders = []
        # not_real_orders = []
        # for p_food in possible_foods:
        #     food_status = False
        #     for f in self.food_menu:
        #         if f.name == p_food:
        #             current_table.food_orders.append(f)
        #             real_orders.append(f)
        #             food_status = True
        #     if not food_status:
        #         not_real_orders.append(p_food)
        #
        # return_result = [f"Table {table_number} ordered:"]
        # for foodz in real_orders:
        #     return_result.append(repr(foodz))
        #
        # return_result.append(f"{self.name} does not have in the menu:")
        # for not_foodz in not_real_orders:
        #     return_result.append(not_foodz)
        #
        # return "\n".join(return_result)

        if table_number not in [t.table_number for t in self.tables_repository]:
            return f"Could not find table {table_number}"

        current_table = [t for t in self.tables_repository if t.table_number == table_number][0]

        possible_foods = list(food_names)
        not_real_orders = []
        for p_food in possible_foods:
            if p_food in [f.name for f in self.food_menu]:
                food = [f for f in self.food_menu if f.name == p_food][0]
                current_table.order_food(food)
            else:
                not_real_orders.append(p_food)

        return_result = [f"Table {table_number} ordered:"]
        for foodz in current_table.food_orders:
            return_result.append(repr(foodz))

        return_result.append(f"{self.name} does not have in the menu:")
        for not_foodz in not_real_orders:
            return_result.append(not_foodz)

        return "\n".join(return_result)

    def order_drink(self, table_number: int, *drinks_names):
        if table_number not in [t.table_number for t in self.tables_repository]:
            return f"Could not find table {table_number}"

        current_table = [t for t in self.tables_repository if t.table_number == table_number][0]

        possible_drinks = list(drinks_names)
        not_real_orders = []

        for p_drink in possible_drinks:
            if p_drink in [d.name for d in self.drinks_menu]:
                drink = [d for d in self.drinks_menu if d.name == p_drink][0]
                current_table.order_drink(drink)
            else:
                not_real_orders.append(p_drink)

        return_result = [f"Table {table_number} ordered:"]
        for drinkz in current_table.drink_orders:
            return_result.append(repr(drinkz))

        return_result.append(f"{self.name} does not have in the menu:")
        for not_drinkz in not_real_orders:
            return_result.append(not_drinkz)

        return "\n".join(return_result)

    def leave_table(self, table_number: int):
        current_table = [t for t in self.tables_repository if t.table_number == table_number][0]
        bill = current_table.get_bill()
        current_table.clear()
        self.total_income += bill

        return_result = [f"Table: {table_number}", f"Bill: {bill:.2f}"]
        return "\n".join(return_result)

    def get_free_tables_info(self):
        return_result = []
        # ordered_tables = sorted(self.tables_repository, key=lambda x: x.table_number)
        for t in self.tables_repository:
            if t.number_of_people == 0:
                return_result.append(t.free_table_info())

        return "\n".join(return_result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"


# a = Bakery("me")
# a.add_table("OutsideTable", 93, 12)
# a.add_table("OutsideTable", 53, 11)
# a.add_table("OutsideTable", 73, 10)
# print(a.get_free_tables_info())
# a = 5
