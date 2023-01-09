import tkinter as tk
from PIL import Image, ImageTk


class Player_bar:
    def __init__(self, frame: tk.Frame) -> None:
        self.FONT = ("Arial", 20)
        self.frame = frame

        self.switch_var = 0

    def build(self, image: str, name: str, 
              time: bool | int, undo_func, color: str) -> tk.Frame:
        self.p1_frame = tk.Frame(master=self.frame, bg='black')

        self.img = ImageTk.PhotoImage(Image.open(image))

        self.player_label = tk.Label(
            master=self.p1_frame,
            image=self.img,
            bg='black'
        )
        self.player_label.pack()

        self.name_label = tk.Label(
            master=self.p1_frame,
            font=self.FONT,
            text=name,
            bg='black',
            fg=color
        )
        self.name_label.pack()

        self.sign_label = tk.Label(master=self.p1_frame, bg='black')
        self.sign_label.pack()

        self.time_label = tk.Label(
            master=self.p1_frame,
            bg='black',
            font=self.FONT,
            fg='orange',
            text=('%02d:%02d' % (time // 60, time % 60))
        )
        self.time_label.pack()

        self.undo_button = tk.Button(
            master=self.p1_frame,
            font=self.FONT,
            text='Undo',
            bg='black',
            fg=color,
            activebackground='black',
            activeforeground=color,
            command=undo_func
        )
        self.undo_button.pack()

        return self.p1_frame

    def set_time(self, time: int) -> None:
        self.time_label.config(text=time)

    def set_sign(self, img: str) -> None:
        image = ImageTk.PhotoImage(Image.open(img))
        self.sign_label.config(image=image)

    def switch(self) -> None:
        if self.switch_var % 2 == 0:
            self.player_label.config(bg='yellow')
        else:
            self.player_label.config(bg='black')
        self.switch_var += 1
        pass
