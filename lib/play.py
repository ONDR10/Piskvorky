import lib.pisqworky
from lib.game import Playing_field
from lib.pisqworky import Desk

class Play:
    def __init__(self, window, player1, player2, time: int, home_func) -> None:
        self.window = window
        self.player1 = player1
        self.player2 = player2
        self.time = time
        self.home_func = home_func

        self.playground = Playing_field(self.window, player1, player2)
        self.desk = Desk()

        self.window.bind('<Escape>', self.pause)
        self.window.bind('<p>', self.pause)

        self.num_of_games = 0

        self.player1.turn = 1
        self.player2.turn = 0


    def build_field(self) -> None:
        self.playground.build(
            self.turn,
            self.time,
            self.time,
            self.player1.img,
            self.player2.img,
            self.undo
        )
        self.playground.switch(self.player1.turn == 1)
        self.player1.sign = 0
        self.player2.sign = 0
    
    def turn(self, x: int, y: int) -> None:
        if self.desk.status:
            return
        num_moves = self.desk.get_num_of_moves()
        if num_moves > 2 and self.player1.sign:
            self.move(x, y)
            self.playground.switch()
        elif num_moves == 2:
            self.move(x, y)
            self.playground.switch()
            self.choose_frame = self.playground.choose_sign(
                self.player1.turn,
                self.playground.switch
            )
        elif num_moves == 4:
            self.move(x, y)
            self.playground.switch()
            self.playground.choose_sign(
                self.player1.turn,
                self.playground.switch
            )
        elif num_moves < 2 or num_moves == 3:
            self.move(x, y)
            try:
                self.choose_frame.destroy()
            except:
                pass
        

    def undo(self) -> None:
        if self.desk.get_num_of_moves() > 5 and not self.desk.status:
            field = self.desk.undo()
            self.playground.set_desk(field)
            self.playground.switch()

    def restart(self) -> None:
        self.num_of_games += 1
        self.playground.__init__(self.window, self.player1, self.player2)
        self.playground.build(
            self.turn,
            self.time,
            self.time,
            self.player1.img,
            self.player2.img,
            self.undo
        )
        self.desk.__init__()
        self.playground.switch(self.player1.turn == 1)
        self.player1.sign = 0
        self.player2.sign = 0

    def win(self, status: int) -> None:
        self.playground.win(
            status,
            self.home_func,
            self.restart
        )

    def move(self, x, y) -> None:
        if self.desk.status:
            return
        data, status = self.desk.turn(x, y)
        if not status:
            self.playground.set_desk(data)
        else:
            self.playground.set_desk(data)
            self.win(status)

    def pause(self, event) -> None:
        if not self.desk.status:
            self.playground.pause(self.home_func, self.restart, self.desk)
