from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []
        self.health_points = 0
        self.damage_points = 0

    @property
    def health_points(self):
        return sum([c.health_points for c in self.cards])

    @property
    def damage_points(self):
        return sum([c.damage_points for c in self.cards])

    def add(self, card: Card):
        if card.name in [c.name for c in self.cards]:
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        current_card = [c for c in self.cards if c.name == card][0]
        self.cards.remove(current_card)
        self.count -= 1

    def find(self, name):
        current_card = [c for c in self.cards if c.name == name][0]
        return current_card

    @health_points.setter
    def health_points(self, value):
        self._health_points = value

    @damage_points.setter
    def damage_points(self, value):
        self._damage_points = value
