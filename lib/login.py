import tkinter as tk
import pandas as pd
from PIL import Image, ImageTk
from functools import partial


class Login:
    def __init__(self, window, data_path: str, bg_image: str) -> None:
        self.window = window
        self.path = data_path
        
        self.FONT2 = ("Arial", 28)
        self.FONT = ("Arial", 26)

        self.bg_login_img = ImageTk.PhotoImage(Image.open(bg_image))

    def build(self, func, player) -> None:
        self.window.minsize(720, 405)

        background_label = tk.Label(master=self.window, image=self.bg_login_img)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        username = tk.StringVar()
        name_entry = tk.Entry(
            master=self.window,
            font=self.FONT2,
            textvariable=username,
            bg='#05f7d9',
            fg='red')

        password = tk.StringVar()
        password_entry = tk.Entry(
            master=self.window,
            font=self.FONT2,
            textvariable=password,
            bg='#f705b4',
            fg='blue'
        )

        name_label = tk.Label(
            master=self.window,
            text="Name: ",
            font=self.FONT,
            bg='#080808',
            fg='blue'
        )

        password_label = tk.Label(
            master=self.window,
            text="Password: ",
            font=self.FONT,
            bg='#080808',
            fg='red'
        )

        self.error = tk.StringVar()
        error_label = tk.Label(
            master=self.window,
            text='',
            font=self.FONT,
            textvariable=self.error,
            bg='black',
            fg='white'
        )

        self.login = partial(self.login, username, password, func, player)
        self.register = partial(self.register, username, password)

        loggin_button = tk.Button(
            master=self.window,
            text='Sign in',
            font=self.FONT,
            command=self.login,
            bg='#080808',
            fg='blue',
            activebackground='#080808',
            activeforeground='red'
        )

        register_button = tk.Button(
            master=self.window,
            text='Sign up',
            font=self.FONT,
            command=self.register,
            bg='#080808',
            fg='red',
            activebackground='#080808',
            activeforeground='blue'
        )

        name_label.place(relx=.5, rely=.1, anchor="center")
        name_entry.place(relx=.5, rely=.25, anchor="center")
        password_label.place(relx=.5, rely=.4, anchor="center")
        password_entry.place(relx=.5, rely=.55, anchor="center")
        loggin_button.place(relx=.40, rely=.75, anchor="center")
        register_button.place(relx=.60, rely=.75, anchor="center")
        error_label.place(relx=.5, rely=.9, anchor="center")

    def login(self, username: tk.StringVar, password: tk.StringVar, home, player) -> None:
        username, password = username.get(), password.get()

        try:
            df = pd.read_csv(self.path)
        except:
            self.error.set("You have to sign up first")
            return

        data = df.loc[df['name'] == username].to_dict('records')

        if data:
            data = data[0]
        if not data:
            self.error.set('Wrong name')
            return
        if data['password'] != password:
            self.error.set('Wrong password')
            return
        else:
            player.__init__(data['id'], data['name'], data['elo'], 'player1.png')
            home()

    def register(self, username: tk.StringVar, password: tk.StringVar) -> None:
        username, password = username.get(), password.get()

        try:
            df = pd.read_csv(self.path)
            name_list = df[['name']].to_dict('records')
        except FileNotFoundError:
            with open(self.path, "w") as file:
                file.write("id,name,password,elo,win,lose\n")
            df = pd.read_csv(self.path)
            name_list = None

        if name_list:
            names = list()
            for di in name_list:
                names.append(di['name'])

            if username in names:
                self.error.set('you are already registered')
                return

        if not username:
            self.error.set('Wrong name')
            return

        if len(str(password)) < 4:
            self.error.set('Try longer password')
            return

        ndf = pd.DataFrame({
            'name': username,
            'password': password,
            'elo': 950,
            'win': 0,
            'lose': 0
            }, index=[len(df.index) + 1])
        ndf.to_csv(self.path, mode='a', header=False)

        self.error.set('you are successfully registered')
