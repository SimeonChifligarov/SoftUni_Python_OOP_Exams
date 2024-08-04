from project.player.player import Player


class Advanced(Player):
    def __init__(self, username):
        super().__init__(username, 250)
