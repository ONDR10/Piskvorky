class Player:
    def __init__(self, id: int, name: str, elo: int, img: str) -> None:
        self.id = id
        self.name = name
        self.elo = elo
        self.img = f'images\\{img}'