class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food_list = [obj for obj in self.supplies if type(obj).__name__ == "FoodSupply"]
        if not food_list:
            raise IndexError("There are no food supplies left!")

        return food_list

    # @food.setter
    # def food(self):
    #     if not [obj for obj in self.supplies if obj.__class__.__name == "Food"]:
    #         raise IndexError("There are no food supplies left!")
    #
    #     self.__food = [obj for obj in self.supplies if obj.__class__.__name == "Food"]

    @property
    def water(self):
        water_list = [obj for obj in self.supplies if type(obj).__name__ == "WaterSupply"]
        if not water_list:
            raise IndexError("There are no water supplies left!")

        return water_list

    # @water.setter
    # def water(self):
    #     if not [obj for obj in self.supplies if obj.__class__.__name__ == "Water"]:
    #         raise IndexError("There are no water supplies left!")
    #
    #     self.__water = [obj for obj in self.supplies if obj.__class__.__name__ == "Water"]
    
    @property
    def painkillers(self):
        painkillers_list = [obj for obj in self.medicine if type(obj).__name__ == "Painkiller"]
        if not painkillers_list:
            raise IndexError("There are no painkillers left!")

        return painkillers_list

    # @painkillers.setter
    # def painkillers(self):
    #     if not [obj for obj in self.medicine if obj.__class__.__name__ == "Painkiller"]:
    #         raise IndexError("There are no painkillers left!")
    #
    #     self.__painkillers = [obj for obj in self.medicine if obj.__class__.__name__ == "Painkiller"]

    @property
    def salves(self):
        salves_list = [obj for obj in self.medicine if type(obj).__name__ == "Salve"]
        if not salves_list:
            raise IndexError("There are no salves left!")

        return salves_list

    # @salves.setter
    # def salves(self):
    #     if not [obj for obj in self.medicine if obj.__class__.__name__ == "Salve"]:
    #         raise IndexError("There are no salves left!")
    #
    #     self.__salves = [obj for obj in self.medicine if obj.__class__.__name__ == "Salve"]

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")

        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        if survivor.needs_healing:
            medicine_of_interest = None
            if medicine_type == "Painkiller":
                medicine_of_interest = self.painkillers.pop()
            elif medicine_type == "Salve":
                medicine_of_interest = self.salves.pop()
            medicine_of_interest.apply(survivor)
            self.medicine.remove(medicine_of_interest)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        if survivor.needs_sustenance:
            sustenance_of_interest = None
            if sustenance_type == "FoodSupply":
                sustenance_of_interest = self.food.pop()
            elif sustenance_type == "WaterSupply":
                sustenance_of_interest = self.water.pop()
            sustenance_of_interest.apply(survivor)
            self.supplies.remove(sustenance_of_interest)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for current_survivor in self.survivors:
            current_survivor.needs -= current_survivor.age * 2

        for current_survivor in self.survivors:

            # if self.food:
            #     food = self.food.pop(0)
            #     self.supplies.remove(food)
            #     food.apply(current_survivor)
            # if self.water:
            #     water = self.water.pop(0)
            #     self.supplies.remove(water)
            #     water.apply(current_survivor)

            self.sustain(current_survivor, "FoodSupply")
            self.sustain(current_survivor, "WaterSupply")
