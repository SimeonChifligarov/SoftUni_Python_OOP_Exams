# class PetShop:
#     def __init__(self, name: str):
#         self.name = name
#         self.food = {}
#         self.pets = []

#     def add_food(self, name: str, quantity: float):
#         if quantity <= 0:
#             raise ValueError('Quantity cannot be equal to or less than 0')

#         if name not in self.food:
#             self.food[name] = 0
#         self.food[name] += quantity
#         return f"Successfully added {quantity:.2f} grams of {name}."

#     def add_pet(self, name: str):
#         if name not in self.pets:
#             self.pets.append(name)
#             return f"Successfully added {name}."
#         raise Exception("Cannot add a pet with the same name")

#     def feed_pet(self, food_name: str, pet_name: str):
#         if pet_name not in self.pets:
#             raise Exception(f"Please insert a valid pet name")

#         if food_name not in self.food:
#             return f'You do not have {food_name}'

#         if self.food[food_name] < 100:
#             self.add_food(food_name, 1000.00)
#             return "Adding food..."

#         self.food[food_name] -= 100
#         return f"{pet_name} was successfully fed"

#     def __repr__(self):
#         return f'Shop {self.name}:\n' \
#                f'Pets: {", ".join(self.pets)}'


from unittest import TestCase, main

from project.pet_shop import PetShop


class TestPetShop(TestCase):
    def setUp(self):
        self.petshop = PetShop("turbo pet")

    def test_init(self):
        new_petshop = PetShop("mega giga turbo pet")
        self.assertEqual("mega giga turbo pet", new_petshop.name)
        self.assertEqual({}, new_petshop.food)
        self.assertEqual([], new_petshop.pets)

    def test_add_food_with_negative_quantity_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.petshop.add_food("mandja1", -5)
        self.assertEqual("Quantity cannot be equal to or less than 0", str(ex.exception))
        self.assertEqual({}, self.petshop.food)

    def test_add_food_nonexisting_valid(self):
        self.assertEqual({}, self.petshop.food)
        actual_result = self.petshop.add_food("mandja1", 2)
        expected_result = "Successfully added 2.00 grams of mandja1."
        self.assertEqual({"mandja1": 2}, self.petshop.food)
        self.assertEqual(expected_result, actual_result)

    def test_add_food_existing_valid(self):
        self.assertEqual({}, self.petshop.food)
        actual_result = self.petshop.add_food("mandja1", 2)
        expected_result = "Successfully added 2.00 grams of mandja1."
        self.assertEqual({"mandja1": 2}, self.petshop.food)
        self.assertEqual(expected_result, actual_result)
        actual_result_second = self.petshop.add_food("mandja1", 20)
        expected_result_second = "Successfully added 20.00 grams of mandja1."
        self.assertEqual({"mandja1": 22}, self.petshop.food)
        self.assertEqual(expected_result_second, actual_result_second)

    def test_add_pet_existing_raises(self):
        self.assertEqual([], self.petshop.pets)
        self.petshop.add_pet("messi")
        self.assertEqual(["messi"], self.petshop.pets)
        with self.assertRaises(Exception) as ex:
            self.petshop.add_pet("messi")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))
        self.assertEqual(["messi"], self.petshop.pets)

    def test_add_pet_valid(self):
        self.assertEqual([], self.petshop.pets)
        actual_result = self.petshop.add_pet("messi")
        expected_result = "Successfully added messi."
        self.assertEqual(["messi"], self.petshop.pets)
        self.assertEqual(expected_result, actual_result)

    def test_feed_pet_nonexisting_pet_raises(self):
        with self.assertRaises(Exception) as ex:
            self.petshop.feed_pet("food1", "pet1")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_nonexisting_food_raises(self):
        self.petshop.pets = ["konche"]
        actual_result = self.petshop.feed_pet("mandjaz", "konche")
        expected_result = "You do not have mandjaz"
        self.assertEqual(expected_result, actual_result)

    def test_feed_pet_low_quantity_food(self):
        self.petshop.pets = ["slavi"]
        self.petshop.food = {"mand": 20}
        actual_result = self.petshop.feed_pet("mand", "slavi")
        expected_result = "Adding food..."
        # self.petshop.food = {"mand": 1020.00}
        self.assertEqual(expected_result, actual_result)
        self.assertEqual({"mand": 1020.00}, self.petshop.food)

    def test_feed_pet_high_quantity_food(self):
        self.petshop.pets = ["slavi"]
        self.petshop.food = {"mand": 200}
        actual_result = self.petshop.feed_pet("mand", "slavi")
        expected_result = "slavi was successfully fed"
        self.assertEqual(expected_result, actual_result)
        self.assertEqual({"mand": 100}, self.petshop.food)

    def test_repr_one_pet(self):
        self.petshop.pets = ["slavi", "tosho"]
        expected_result = "Shop turbo pet:\nPets: slavi, tosho"
        self.assertEqual(expected_result, repr(self.petshop))


if __name__ == '__main__':
    main()
