class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_expenses = 0
        for current_room in self.rooms:
            current_room_total_expenses = current_room.expenses + current_room.room_cost
            total_expenses += current_room_total_expenses
        return f"Monthly consumption: {total_expenses:.2f}$."

    def pay(self):
        information_for_rooms = []
        for current_room in self.rooms:
            if current_room.budget < current_room.expenses + current_room.room_cost:
                information_for_rooms.append(f"{current_room.family_name} does not have "
                                             f"enough budget and must leave the hotel.")
                self.rooms.remove(current_room)
            else:
                current_room.budget -= current_room.expenses + current_room.room_cost
                information_for_rooms.append(
                    f"{current_room.family_name} paid {current_room.expenses + current_room.room_cost:.2f}$ "
                    f"and have {current_room.budget:.2f}$ left."
                )

        return "\n".join(information_for_rooms)

    def status(self):
        status_result = []
        all_guests_in_the_hotel = 0
        for current_room in self.rooms:
            all_guests_in_the_hotel += current_room.members_count

        status_result.append(f"Total population: {all_guests_in_the_hotel}")

        for current_room in self.rooms:
            status_result.append(f"{current_room.family_name} with {current_room.members_count} members. "
                                 f"Budget: {current_room.budget:.2f}$, Expenses: {current_room.expenses:.2f}$")

            if current_room.children:
                for child_idx in range(len(current_room.children)):
                    status_result.append(f"--- Child {child_idx + 1} monthly "
                                         f"cost: {current_room.children[child_idx].get_monthly_expense():.2f}$")

            status_result.append(f"--- Appliances monthly "
                                 f"cost: {current_room.calculate_expenses(current_room.appliances):.2f}$")

        return "\n".join(status_result)
