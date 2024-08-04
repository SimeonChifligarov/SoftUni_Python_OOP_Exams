from unittest import TestCase, main

from project.people.child import Child
from project.rooms.room import Room


class TestRoom(TestCase):
    def setUp(self):
        self.room = Room("Qkata staq", 1000, 4)

    def test_init(self):
        current_room = Room("Opa Udriii", 2000, 8)
        self.assertEqual("Opa Udriii", current_room.family_name)
        self.assertEqual(2000, current_room.budget)
        self.assertEqual(8, current_room.members_count)
        self.assertEqual([], current_room.children)
        self.assertEqual(0, current_room.expenses)

    def test_expenses_property_set_correct(self):
        self.room.expenses = 69
        self.assertEqual(69, self.room.expenses)

    def test_expenses_property_with_negative_number_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -1000
        self.assertEqual("Expenses cannot be negative", str(ex.exception))

    def test_calculate_expenses(self):
        expected_result = 4500
        actual_result = self.room.calculate_expenses([Child(10), Child(20), Child(30), Child(40), Child(50)])
        self.assertEqual(expected_result, actual_result)
        actual_result_second = self.room.calculate_expenses([Child(10), Child(20, 30, 40, 50)])
        self.assertEqual(expected_result, actual_result_second)


if __name__ == '__main__':
    main()
