from project.card.magic_card import MagicCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player import Player


class BattleField:

    @staticmethod
    def fight(attacker: Player, enemy: Player):

        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        for pl in [attacker, enemy]:
            if type(pl).__name__ == "Beginner":
                pl.health += 40
                for c in pl.card_repository.cards:
                    c.damage_points += 30

            pl.health += pl.card_repository.health_points

        while True:
            players_list = [attacker, enemy]
            att_pl = players_list[0]
            def_pl = players_list[1]

            att_damage = att_pl.card_repository.damage_points
            print(att_damage)
            print(def_pl.current_health)

            # try:
            #     def_pl.take_damage(att_damage)
            # except ValueError as ex:
            #     if str(ex) == "Player's health bonus cannot be less than zero ":
            #         break

            def_pl.take_damage(att_damage)

            print(def_pl.current_health)
            if def_pl.is_dead:
                break

            players_list.append(players_list.pop(0))


# p1 = Beginner("gosho")
# c1 = MagicCard("udri")
# p1.card_repository.cards.append(c1)
# p2 = Advanced("tosho")
# bf = BattleField()
# bf.fight(p1, p2)
# a = 5
