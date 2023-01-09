import tkinter as tk
from PIL import ImageTk, Image
from lib.login import Login
from lib.menu import Menu
from lib.player import Player
from lib.play import Play


class App:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title = 'Pisqworky'
        self.window.resizable(False, False)

        self.login = Login(self.window, 'data\\data.csv', 'images\\bg_login.png')
        self.menu = Menu(self.window)

        self.player1 = Player(0, 'GUest1', 'player1.png', 950)
        self.player2 = Player(0, 'Guest2', 'player2.png', 950)

    def clear_screen(self):
        for widgets in self.window.winfo_children():
            widgets.destroy()

    def home(self):
        self.clear_screen()
        self.menu.build(self.player_vs_player)

    def player_vs_player(self):
        self.clear_screen()
        self.player2.__init__(0, 'Guest', 950, 'player2.png')
        self.play = Play(self.window, self.player1, self.player2, 0, self.home)
        self.play.build_field()

    def run(self):
        self.login.build(self.home, self.player1)
        self.window.mainloop()