import tkinter as tk
from PIL import Image, ImageTk
from typing import List


class Grafic_desk:
    def __init__(self, frame: tk.Frame) -> None:
        self.empty_place_img = ImageTk.PhotoImage(Image.open("images\\empty_place.png"))
        self.o_img = ImageTk.PhotoImage(Image.open('images\\o_min.png'))
        self.x_img = ImageTk.PhotoImage(Image.open('images\\x_min.png'))

        self.frame = frame

    def build(self, command):
        playing_field = tk.Frame(master=self.frame, width=510, height=510)

        self.play_button_list = list()
        for i in range(15):
            for j in range(15):
                def func(x=i, y=j):
                    return command(x, y)

                self.play_button_list.append(
                    tk.Button(
                        master=playing_field,
                        image=self.empty_place_img,
                        bg='black',
                        width=34,
                        height=34,
                        command=func
                    )
                )
                self.play_button_list[-1].grid(row=i, column=j)

        return playing_field

    def reload(self, data: List[List[tk.Button]]) -> None:
        for i, row in enumerate(data):
            for j, button in enumerate(row):
                self.play_button_list[i*15+j].config(
                    image=self.x_img if button == 1 else self.o_img if button == 2 else self.empty_place_img
                )
