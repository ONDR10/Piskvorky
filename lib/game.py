import tkinter as tk
from PIL import Image, ImageTk
from lib.desk import Grafic_desk
from lib.player_bar import Player_bar
from typing import List

class Playing_field:
    def __init__(self, frame: tk.Frame | tk.Tk, player1, player2) -> None:
        self.player1 = player1
        self.player2 = player2
        self.frame = frame

        self.FONT = ("Arial", 26)

        self.x_img = ImageTk.PhotoImage(
            Image.open("images\\x_min.png")
        )
        self.o_img = ImageTk.PhotoImage(
            Image.open("images\\o_min.png")
        )

        self.desk_bg_img = ImageTk.PhotoImage(
            Image.open("images\\bg_desk.png")
        )

        self.switch_var = 0

    def build(self, move, time1: int, time2: int, 
              p1_image: str, p2_image: str, undo_func) -> None:

        self.desk = Grafic_desk(self.frame)
        self.p_bar1 = Player_bar(self.frame)
        self.p_bar2 = Player_bar(self.frame)

        self.bg_label = tk.Label(master=self.frame, image=self.desk_bg_img)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame_desk = self.desk.build(move)
        self.frame_desk.place(relx=.5, rely=.5, anchor='center')

        self.frame_p_bar1 = self.p_bar1.build(
            p1_image,
            self.player1.name,
            time1,
            undo_func,
            'red'
        )
        self.frame_p_bar1.place(relx=.1, rely=.5, anchor='center')

        self.frame_p_bar2 = self.p_bar2.build(
            p2_image,
            self.player2.name,
            time2,
            undo_func,
            'blue'
        )
        self.frame_p_bar2.place(relx=.9, rely=.5, anchor='center')

    def set_time(self, time1: int, time2: int) -> None:
        self.p_bar1.set_time(time1)
        self.p_bar2.set_time(time2)

    def set_signs(self, img1: str, img2: str) -> None:
        self.p_bar1.set_sign(img1)
        self.p_bar2.set_sign(img2)

    def set_desk(self, data: List[List[int]]) -> None:
        self.desk.reload(data)

    def switch(self, con: bool = None) -> None:
        self.player1.turn = (self.player1.turn + 1) % 2
        self.player2.turn = (self.player2.turn + 1) % 2

        if self.switch_var == 0:
            if con:
                self.p_bar1.switch()
            else:
                self.p_bar2.switch()
        else:
            self.p_bar1.switch()
            self.p_bar2.switch()
        self.switch_var += 1

    def win(self, status: int, home_func, reset_func) -> None:
        def restart():
            self.win_frame.destroy()
            reset_func()
        
        self.switch()

        self.win_frame = tk.Frame(
            master=self.frame,
            bg='#161616',
            highlightbackground='yellow',
            border=1
        )
        self.win_frame.place(relx=.5, rely=.5, anchor='center')
        
        win_label = tk.Label(
            master=self.win_frame,
            font=self.FONT,
            bg='#161616',
            fg='red' if status == self.player1.sign else 'blue',
            text=f'Congratulation \
\n{self.player1.name if self.player1.sign == status else self.player2.name} \
\nYOU WON'
        )
        win_label.pack()
        
        button_frame = tk.Frame(master=self.win_frame)
        button_frame.pack()
        
        exit_button = tk.Button(
            master=button_frame,
            font=self.FONT,
            bg='#161616',
            fg='purple',
            text='Exit',
            command=home_func
        )
        exit_button.pack(side='left')

        play_again_button = tk.Button(
            master=button_frame,
            font=self.FONT,
            bg='#161616',
            fg='yellow',
            text='Play again',
            command=restart
        )
        play_again_button.pack(side='left')

    def choose_sign(self, side: bool, func_swap) -> tk.Frame:
        def command(player1, player2, sign, side, func) -> None:
            if not side:
                player1.sign = sign
                player2.sign = 2 if sign == 1 else 1
            else:
                player1.sign = 2 if sign == 1 else 1 
                player2.sign = sign
            if sign == 1:
                func()
            self.frame_choose.destroy()

        self.frame_choose = tk.Frame(master=self.frame)

        button_x = tk.Button(
            master=self.frame_choose,
            command=lambda: command(self.player1, self.player2, 1, side, func_swap),
            image=self.x_img,
            bg='yellow'
        )
        button_x.pack(side='left')
        
        button_o = tk.Button(
            master=self.frame_choose,
            command=lambda: command(self.player1, self.player2, 2, side, func_swap),
            image=self.o_img,
            bg='yellow'
        )
        button_o.pack(side='left')
        
        self.frame_choose.place(
            relx=.9 if side else .1,
            rely=.9,
            anchor='center'
        )

        return self.frame_choose

    def pause(self, home_func, reset_func, desk) -> None:
        desk.status = 3

        self.pause_frame = tk.Frame(
            master=self.frame,
            bg='#161616',
            highlightbackground='yellow',
            border=1
        )
        self.pause_frame.place(relx=.5, rely=.5, anchor='center')

        def restart():
            self.pause_frame.destroy()
            reset_func()

        def cont_func():
            self.pause_frame.destroy()
            desk.status = 0

        pause_label = tk.Label(
            master=self.pause_frame,
            font=self.FONT,
            bg='#161616',
            fg='Orange',
            text='PAUSE',
            border=20
        )
        pause_label.grid(row=0, column=0, sticky='news')

        button_continue = tk.Button(
            master=self.pause_frame,
            font=self.FONT,
            bg='#161616',
            fg='green',
            text='Continue',
            command=cont_func
        )
        button_continue.grid(row=1, column=0, sticky='news')

        play_again_button = tk.Button(
            master=self.pause_frame,
            font=self.FONT,
            bg='#161616',
            fg='yellow',
            text='Play again',
            command=restart
        )
        play_again_button.grid(row=2, column=0, sticky='news')
        
        exit_button = tk.Button(
            master=self.pause_frame,
            font=self.FONT,
            bg='#161616',
            fg='red',
            text='Exit',
            command=home_func
        )
        exit_button.grid(row=3, column=0, sticky='news')
