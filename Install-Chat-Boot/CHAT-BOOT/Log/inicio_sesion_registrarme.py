"""Creación y inicio de Sesion en Cuenta del usuario"""


from tkinter import Tk, Label, PhotoImage, Entry, StringVar, Button, messagebox, Toplevel
import sqlite3

windows = Tk()
Username = StringVar()
Password = StringVar()
Searches = StringVar()
# Registrarme


class Registrarme():

    '''Aquí el usuario se registrara con sus datos que elija'''

    def __init__(
            self
    ):

        # Visual

        self.root = Toplevel()
        self.root.geometry(
            '1000x600+425+245'
        )
        self.root.resizable(
            False,
            False
        )
        self.root.title(
            'Registrarme'
        )
        self.root.iconbitmap(
            r'images\icon-user.ico'
        )
        self.root.config(
            background='#202123'
        )

        # Panel

        panel = Label(
            self.root,
            background='#232a38'
        )

        panel.place(
            width=400,
            height=600,
            x=0,
            y=0
        )

        # Logo

        logo_img = PhotoImage(
            file=r'images\logo-robot.png'
        )

        logo = Label(
            self.root,
            image=logo_img,
            background='#202123'
        )

        logo.place(
            x=443,
            y=53
        )

        # IniciarSesión -> Txt

        iniciar_sesion_txt = Label(
            self.root,
            text='Sign Up',
            font=(
                'Arial Black', 40
            ),
            background='#232a38',
            foreground='white'
        )

        iniciar_sesion_txt.place(
            x=85,
            y=30
        )

        # IniciarSesión -> Username

        iniciar_txt_username = Label(
            self.root,
            text='Usuario',
            font=(
                'Arial', 18
            ),
            background='#232a38',
            foreground='white'
        )

        iniciar_txt_username.place(
            x=50,
            y=150
        )

        self.iniciar_entry_username = Entry(
            self.root,
            textvariable=Username,
            font=(
                'Arial', 18
            ),
            background='#202123',
            foreground='white',
            justify='center'
        )

        self.iniciar_entry_username.place(
            width=300,
            x=47,
            y=190
        )

        # IniciarSesión -> Password

        iniciar_txt_password = Label(
            self.root,
            text='Contraseña',
            font=(
                'Arial', 18
            ),
            background='#232a38',
            foreground='white'
        )

        iniciar_txt_password.place(
            x=50,
            y=250
        )

        self.iniciar_entry_password = Entry(
            self.root,
            textvariable=Password,
            font=(
                'Arial', 18
            ),
            background='#202123',
            foreground='white',
            justify='center',
            show=(
                '*'
            )
        )

        self.iniciar_entry_password.place(
            width=300,
            x=47,
            y=290
        )

        # No ver contraseña -> Ver contraseña

        no_ver_password_txt = Label(
            self.root,
            text='Ver Contraseña',
            font=(
                'Arial', 14
            ),
            background='#232a38',
            foreground='white'
        )

        no_ver_password_txt.place(
            x=100,
            y=343
        )

        no_ver_password_bt = Button(
            self.root,
            background='white',
            cursor='hand2',
            activebackground='grey',
            border=0,
            command=lambda: [
                {
                    self.ver_contra()
                }
            ]
        )

        no_ver_password_bt.place(
            width=15,
            height=15,
            x=70,
            y=350
        )

        # Registrarse -> Boton

        self.boton_registrarme = Button(
            self.root,
            text='Registrarme',
            font=(
                'Arial Black', 14
            ),
            background='#202123',
            foreground='white',
            activebackground='white',
            activeforeground='grey',
            cursor='hand2',
            command=lambda: self.registrarme(
                Username.get(), Password.get()
            )
        )

        self.boton_registrarme.place(
            width=300,
            x=50,
            y=430
        )

        # IniciarSesión -> Botón

        boton_iniciar_sesion = Button(
            self.root,
            text='Iniciar Sesión',
            font=(
                'Arial Black', 14
            ),
            background='white',
            foreground='grey',
            activebackground='#202123',
            activeforeground='white',
            cursor='hand2',
            command=lambda: [
                {
                    self.iniciar_sesion_boton()
                }
            ]
        )

        boton_iniciar_sesion.place(
            width=300,
            x=50,
            y=500
        )
        # Funciones del teclado

        self.root.bind(
            '<Return>', self.registrarme_teclado
        )

        self.root.mainloop()

    def ver_contra(self):
        '''El usuario vera la contraseña'''
        self.iniciar_entry_password.config(
            show=(
                ''
            )
        )
        ver_password_bt = Button(
            self.root,
            background='grey',
            cursor='hand2',
            activebackground='white',
            command=lambda: [
                {
                    self.no_ver_contra()
                }
            ],
            border=0
        )

        ver_password_bt.place(
            width=15,
            height=15,
            x=70,
            y=350
        )

    def no_ver_contra(self):
        '''El usuario no vera la contraseña'''
        self.iniciar_entry_password.config(
            show=(
                '*'
            )
        )
        no_ver_password_bt = Button(
            self.root,
            background='white',
            cursor='hand2',
            activebackground='grey',
            command=lambda: [
                {
                    self.ver_contra()
                }
            ],
            border=0
        )

        no_ver_password_bt.place(
            x=70,
            y=350,
            width=15,
            height=15
        )

    def registrarme_teclado(self, event):
        '''Presiona un boton al interactuar con el return del teclado'''
        self.boton_registrarme.invoke()

        if event:
            pass

    def iniciar_sesion_boton(self):
        '''El usuario regresara al inicio de sesion'''
        self.root.withdraw()
        self.iniciar_entry_username.delete(
            0,
            'end'
        )
        self.iniciar_entry_password.delete(
            0,
            'end'
        )
        windows.deiconify()
        InicioSesion()

    def registrarme(self, usuario, contra):
        '''Aquí el usuario se podrá registrar'''
        conectar = sqlite3.connect(
            r'Database\users_passwords.db'
        )
        cursor = conectar.cursor()

        cursor.execute(
            "SELECT * FROM user_password WHERE Username = ? AND Password = ?", (
                usuario, contra
            )
        )

        resultado = cursor.fetchall()

        if resultado:
            messagebox.showerror(
                'ERROR', f'El usuario [{Username.get()}] ya esta registrado en esta aplicación'
            )
            self.iniciar_entry_password.delete(
                0,
                'end'
            )
            self.iniciar_entry_password.delete(
                0,
                'end'
            )
            self.root.destroy()
            windows.deiconify()
            InicioSesion()
        else:
            messagebox.showinfo(
                'CONGRATULATIONS', f'Felicidades se registro el usuario [{Username.get()}]'
            )
            cursor.execute(
                f"INSERT INTO user_password VALUES ('{Username.get()}','{Password.get()}')"
            )
            conectar.commit()
            cursor.close()
            self.iniciar_entry_username.delete(
                0,
                'end'
            )
            self.iniciar_entry_password.delete(
                0,
                'end'
            )
            self.root.destroy()
            windows.deiconify()
            InicioSesion()

# Inicio de Sesion


class InicioSesion():

    '''El usuario iniciara sesión con su cuenta'''

    def __init__(
            self
    ):

        # Visual

        windows.geometry(
            '1000x600+425+245'
        )
        windows.resizable(
            False,
            False
        )
        windows.title(
            'IniciarSesión'
        )
        windows.iconbitmap(
            r'images\icon-user.ico'
        )
        windows.config(
            background='#202123'
        )

        # Panel

        panel = Label(
            windows,
            background='#232a38'
        )

        panel.place(
            width=400,
            height=600,
            x=0,
            y=0
        )

        # Logo

        logo_img = PhotoImage(
            file=r'images\logo-robot.png'
        )

        logo = Label(
            windows,
            image=logo_img,
            background='#202123'
        )

        logo.place(
            x=443,
            y=53
        )

        # IniciarSesión -> Txt

        iniciar_sesion_txt = Label(
            windows,
            text='Log In',
            font=(
                'Arial Black', 40
            ),
            background='#232a38',
            foreground='white'
        )

        iniciar_sesion_txt.place(
            x=105,
            y=30
        )

        # IniciarSesión -> Username

        iniciar_txt_username = Label(
            windows,
            text='Usuario',
            font=(
                'Arial', 18
            ),
            background='#232a38',
            foreground='white'
        )

        iniciar_txt_username.place(
            x=50,
            y=150
        )

        self.iniciar_entry_username = Entry(
            windows,
            textvariable=Username,
            font=(
                'Arial', 18
            ),
            background='#202123',
            foreground='white',
            justify='center'
        )

        self.iniciar_entry_username.place(
            width=300,
            x=47,
            y=190
        )

        # IniciarSesión -> Password

        iniciar_txt_password = Label(
            windows,
            text='Contraseña',
            font=(
                'Arial', 18
            ),
            background='#232a38',
            foreground='white'
        )

        iniciar_txt_password.place(
            x=50,
            y=250
        )

        self.iniciar_entry_password = Entry(
            windows,
            textvariable=Password,
            font=(
                'Arial', 18
            ),
            background='#202123',
            foreground='white',
            justify='center',
            show=(
                '*'
            )
        )

        self.iniciar_entry_password.place(
            width=300,
            x=47,
            y=290
        )

        # No ver contraseña -> Ver contraseña

        no_ver_password_txt = Label(
            windows,
            text='Ver Contraseña',
            font=(
                'Arial', 14
            ),
            background='#232a38',
            foreground='white'
        )

        no_ver_password_txt.place(
            x=100,
            y=343
        )

        no_ver_password_bt = Button(
            windows,
            background='white',
            cursor='hand2',
            activebackground='grey',
            border=0,
            command=lambda: [
                {
                    self.ver_contra()
                }
            ]
        )

        no_ver_password_bt.place(
            width=15,
            height=15,
            x=70,
            y=350
        )

        # IniciarSesión -> Botón

        self.boton_iniciar_sesion = Button(
            windows,
            text='Iniciar Sesión',
            font=(
                'Arial Black', 14
            ),
            background='#202123',
            foreground='white',
            activebackground='white',
            activeforeground='grey',
            cursor='hand2',
            command=lambda: self.iniciar_sesion_boton(
                Username.get(), Password.get()
            )
        )

        self.boton_iniciar_sesion.place(
            width=300,
            x=50,
            y=430
        )

        # Registrarse -> Boton

        boton_registrarme = Button(
            windows,
            text='Registrarme',
            font=(
                'Arial Black', 14
            ),
            background='white',
            foreground='grey',
            activebackground='#202123',
            activeforeground='white',
            cursor='hand2',
            command=lambda: [
                {
                    self.registrarme()
                }
            ]
        )

        boton_registrarme.place(
            width=300,
            x=50,
            y=500
        )

        # Funciones del teclado

        windows.bind(
            '<Return>', self.iniciar_sesion_teclado
        )

        windows.mainloop()

    def ver_contra(self):
        '''El usuario vera la contraseña'''
        self.iniciar_entry_password.config(
            show=(
                ''
            )
        )
        ver_password_bt = Button(
            windows,
            background='grey',
            cursor='hand2',
            activebackground='white',
            command=lambda: [
                {
                    self.no_ver_contra()
                }
            ],
            border=0
        )

        ver_password_bt.place(
            width=15,
            height=15,
            x=70,
            y=350
        )

    def no_ver_contra(self):
        '''El usuario no vera la contraseña'''
        self.iniciar_entry_password.config(
            show=(
                '*'
            )
        )
        no_ver_password_bt = Button(
            windows,
            background='white',
            cursor='hand2',
            activebackground='grey',
            command=lambda: [
                {
                    self.ver_contra()
                }
            ],
            border=0
        )

        no_ver_password_bt.place(
            x=70,
            y=350,
            width=15,
            height=15
        )

    def iniciar_sesion_teclado(self, event):
        '''Presiona un boton al interactuar con el return del teclado'''
        self.boton_iniciar_sesion.invoke()

        if event:
            pass

    def iniciar_sesion_boton(self, usuario, contra):
        '''Sirve para que se autorice la entrada a la aplicación con el usuario y contraseña'''

        conectar = sqlite3.connect(
            r'Database\users_passwords.db'
        )
        cursor = conectar.cursor()

        cursor.execute(
            "SELECT * FROM user_password WHERE Username = ? AND Password = ?", (
                usuario, contra
            )
        )

        resultado = cursor.fetchall()

        if resultado:
            messagebox.showinfo(
                "ACEPTADO", f"Has iniciado sesion correctamente con el usuario [{Username.get()}]"
            )
            windows.withdraw()
            import App.chatboot as chatboot
        else:
            messagebox.showerror(
                "DENEGADO", f"El usuario [{Username.get()}] o la contraseña son incorrectos."
            )
            self.iniciar_entry_username.delete(
                0,
                'end'
            )
            self.iniciar_entry_password.delete(
                0,
                'end'
            )

    def registrarme(self):
        '''Aquí el usuario se podrá registrar'''
        windows.withdraw()
        self.iniciar_entry_username.delete(
            0,
            'end'
        )
        self.iniciar_entry_password.delete(
            0,
            'end'
        )
        return Registrarme()


if __name__ == '__main__':
    InicioSesion()
