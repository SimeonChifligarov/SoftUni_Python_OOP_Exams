from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, player_type, username):
        new_player = None
        if player_type == "Beginner":
            new_player = Beginner(username)
        elif player_type == "Advanced":
            new_player = Advanced(username)
        self.player_repository.add(new_player)
        return f"Successfully added player of type {player_type} with username: {username}"

    def add_card(self, card_type, name):
        new_card = None
        if card_type == "Magic":
            new_card = MagicCard(name)
        elif card_type == "Trap":
            new_card = TrapCard(name)
        self.card_repository.add(new_card)
        return f"Successfully added card of type {card_type}Card with name: {name}"

    def add_player_card(self, username, card_name):
        current_card = [c for c in self.card_repository.cards if c.name == card_name][0]
        current_player = [p for p in self.player_repository.players if p.username == username][0]
        current_player.card_repository.add(current_card)
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name, enemy_name):
        attacker = [p for p in self.player_repository.players if p.name == attack_name][0]
        enemy = [p for p in self.player_repository.players if p.name == enemy_name][0]
        bf = BattleField()
        bf.fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        report_result = []

        for pl in self.player_repository.players:
            report_result.append(f"Username: {pl.username} - Health: {pl.health} - Cards {pl.card_repository.count}")

            for crd in pl.card_repository.cards:
                report_result.append(f"### Card: {crd.name} - Damage: {crd.damage_points}")

        # for card in self.card_repository.cards:
        #     report_result.append(f"Card: {card.name} - Damage: {card.damage_points}")

        return "\n".join(report_result)
