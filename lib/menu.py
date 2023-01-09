import tkinter as tk
from PIL import Image, ImageTk


class Menu:
    def __init__(self, window: tk.Frame | tk.Tk) -> None:
        self.window = window

        self.bg_menu_img = ImageTk.PhotoImage(Image.open("images\\bg_menu.png"))
        self.bg_menu_img = tk.PhotoImage(name='bg', file='images\\bg_menu.png')
        self.player_img = ImageTk.PhotoImage(Image.open("images\\player_menu.png"))
        self.bot_img = ImageTk.PhotoImage(Image.open("images\\bot_menu.png"))
        self.settings_img = ImageTk.PhotoImage(Image.open("images\\settings_menu.png"))
        self.profile_img = ImageTk.PhotoImage(Image.open("images\\profile_menu.png"))
        

    def build(self, command) -> None:
        self.window.minsize(1072, 603)

        self.background_label = tk.Label(master=self.window, image=self.bg_menu_img)
        self.play_button = tk.Button(master=self.window, image=self.player_img, fg='blue', bg='blue', activeforeground='red', activebackground='red', command=command)
        self.play_bot_button = tk.Button(master=self.window, image=self.bot_img, fg='blue', bg='blue', activeforeground='red', activebackground='red')
        self.settings_button = tk.Button(master=self.window, image=self.settings_img, fg='blue', bg='blue', activeforeground='red', activebackground='red')
        self.profile_button = tk.Button(master=self.window, image=self.profile_img, fg='blue', bg='blue', activeforeground='red', activebackground='red')

        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.play_button.place(relx=.385, rely=.3, anchor='center')
        self.play_bot_button.place(relx=.615, rely=.3, anchor='center')
        self.settings_button.place(relx=.385, rely=.7, anchor='center')
        self.profile_button.place(relx=.615, rely=.7, anchor='center')