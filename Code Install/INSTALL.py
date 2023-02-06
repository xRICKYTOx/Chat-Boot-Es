from tkinter import *
import tkinter as tk
from tkinter import ttk as ttk
import shutil
import win32api
from tkinter.ttk import *
import time

windows = tk.Tk()
name_pc = win32api.GetUserName()


def exe3():
    class exe3():
        def __init__(
            self
        ):
            self.windows = Toplevel()
            self.windows.geometry(
                '600x500+650+290'
            )
            self.windows.resizable(
                False,
                False
            )
            self.windows.title(
                ''
            )
            self.windows.config(
                background='#232a38'
            )
            self.windows.iconbitmap(
                r'images\update.ico'
            )

            # // Panel / #

            self.panel = tk.Label(
                self.windows,
                background='#202123',
                foreground='#202123'
            )

            self.panel.place(
                x=0,
                y=0,
                width=260,
                height=500
            )

            # // Logo / #

            self.Logo_img = PhotoImage(
                file=r'images\robot.png'
            )

            self.Logo = tk.Label(
                self.windows,
                image=self.Logo_img,
                background='#202123',
                foreground='#202123'
            )

            self.Logo.place(
                x=1,
                y=130
            )

            # // Conitunar / #

            self.continuer = tk.Button(
                self.windows,
                text='SALIR',
                cursor='hand2',
                font=(
                    'Arial', 10
                ),
                background='#232a38',
                foreground='white',
                activeforeground='grey',
                activebackground='white',
                border=0,
                command=lambda: [
                    {
                        self._salir_()
                    }
                ]
            )

            self.continuer.place(
                x=500,
                y=450
            )

            # // Version / #

            self.info = tk.Label(
                self.windows,
                text='GRACIAS POR \nINSTALAR CHAT BOOT',
                background='#232a38',
                foreground='white',
                font=(
                    'Arial Black', 18
                )
            )

            self.info.place(
                x=280,
                y=100
            )

            # // Crear Axesodirecto \\ #

            self.crax_txt = tk.Label(
                self.windows,
                background='#232a38',
                foreground='white',
                text='Crear un acceso directo',
                font=(
                    'Arial', 14
                )
            )

            self.crax_txt.place(
                x=330,
                y=293
            )

            self.crax_bt = tk.Button(
                self.windows,
                background='white',
                command=lambda: [
                    {
                        self.active_crax_bt()
                    }
                ],
                activebackground='grey',
                cursor='hand2',
                border=0
            )

            self.crax_bt.place(
                x=300,
                y=300,
                height=15,
                width=15
            )

            self.windows.mainloop()

        def active_crax_bt(self):
            self.continuer.configure(
                state=DISABLED
            )
            crax_bt = tk.Button(
                self.windows,
                background='grey',
                command=lambda: [
                    {
                        self.desactive_crax_bt()
                    }
                ],
                activebackground='white',
                cursor='hand2',
                border=0
            )

            crax_bt.place(
                x=300,
                y=300,
                height=15,
                width=15
            )
            continuer = tk.Button(
                self.windows,
                text='SALIR',
                cursor='hand2',
                font=(
                    'Arial', 10
                ),
                background='#232a38',
                foreground='white',
                activeforeground='grey',
                activebackground='white',
                border=0,
                command=lambda: [
                    {
                        self._crax_direct_()
                    }
                ]
            )

            continuer.place(
                x=500,
                y=450
            )

        def desactive_crax_bt(self):
            self.continuer.configure(
                state=NORMAL
            )
            crax_bt = tk.Button(
                self.windows,
                background='white',
                command=lambda: [
                    {
                        self.active_crax_bt()
                    }
                ],
                activebackground='grey',
                cursor='hand2',
                border=0
            )

            crax_bt.place(
                x=300,
                y=300,
                height=15,
                width=15
            )
            self.continuer = tk.Button(
                self.windows,
                text='SALIR',
                cursor='hand2',
                font=(
                    'Arial', 10
                ),
                background='#232a38',
                foreground='white',
                activeforeground='grey',
                activebackground='white',
                border=0,
                command=lambda: [
                    {
                        self._salir_()
                    }
                ]
            )

            self.continuer.place(
                x=500,
                y=450
            )

        def _crax_direct_(self):
            folder_path = f"C:/CHAT-BOOT/CHAT-BOOT.lnk"
            destination = f"C:/Users/{name_pc}/OneDrive/Escritorio"
            shutil.move(folder_path, destination)
            return self._salir_()

        def _salir_(self):
            self.windows.destroy()
            windows.destroy()
            exit()

    exe3()


def exe2():
    class exe2():
        def __init__(
            self
        ):
            self.windows = Toplevel()
            self.windows.geometry(
                '600x500+650+290'
            )
            self.windows.resizable(
                False,
                False
            )
            self.windows.title(
                ''
            )
            self.windows.config(
                background='#232a38'
            )
            self.windows.iconbitmap(
                r'images\update.ico'
            )

            # // Panel / #

            self.panel = tk.Label(
                self.windows,
                background='#202123',
                foreground='#202123'
            )

            self.panel.place(
                x=0,
                y=0,
                width=260,
                height=500
            )

            # // Logo / #

            self.Logo_img = PhotoImage(
                file=r'images\robot.png'
            )

            self.Logo = tk.Label(
                self.windows,
                image=self.Logo_img,
                background='#202123',
                foreground='#202123'
            )

            self.Logo.place(
                x=1,
                y=130
            )

            # // Conitunar / #

            self.continuer = tk.Button(
                self.windows,
                text='INSTALAR',
                cursor='hand2',
                font=(
                    'Arial', 10
                ),
                background='#232a38',
                foreground='white',
                activeforeground='grey',
                activebackground='white',
                border=0,
                command=lambda: [
                    {
                        self._install_()
                    }
                ]
            )

            self.continuer.place(
                x=500,
                y=450
            )

            # // Cancelar / #

            self.cancelar = tk.Button(
                self.windows,
                text='REGRESAR',
                cursor='hand2',
                font=(
                    'Arial', 10
                ),
                background='#232a38',
                foreground='white',
                activeforeground='grey',
                activebackground='white',
                border=0,
                command=lambda: [
                    {
                        self._regresar_()
                    }
                ]
            )

            self.cancelar.place(
                x=285,
                y=450
            )

            # // Version / #

            self.ver = tk.Label(
                self.windows,
                text='VER 1.0.0',
                background='#232a38',
                foreground='white',
                font=(
                    'Arial Black', 30
                )
            )

            self.ver.place(
                x=323,
                y=100
            )

            # // Progres Bar / #
            s = ttk.Style()
            s.theme_use('clam')

            s.configure(
                "TProgressbar",
                troughcolor='#202123',
                background='#2b79c2',
                bordercolor="#202123",
            )

            self.bar = ttk.Progressbar(
                self.windows,
                style="TProgressbar",
                orient="horizontal",
                length=315,
            )

            self.bar.place(
                x=273,
                y=350,
                height=30
            )

            self.windows.mainloop()

        def _regresar_(self):
            self.windows.withdraw()
            return exe1()

        def _install_(self):
            self.cancelar.config(
                state=DISABLED
            )
            task = 13
            x = 0
            while (x < task):
                time.sleep(0.5)
                self.bar['value'] += 13
                x += 1.3
                self.windows.update_idletasks()
            else:
                self._move_exe_()

        def _move_exe_(self):
            folder_path = r"CHAT-BOOT"
            destination = r"C:/"
            shutil.move(folder_path, destination)
            self.windows.withdraw()
            return exe3()
    exe2()


def exe1():

    class exe1():
        def __init__(
                self
        ):
            windows.withdraw()
            self.windows = Toplevel()
            self.windows.geometry(
                '600x500+650+290'
            )
            self.windows.resizable(
                False,
                False
            )
            self.windows.title(
                ''
            )
            self.windows.config(
                background='#232a38'
            )
            self.windows.iconbitmap(
                r'images\update.ico'
            )

            # // Panel / #

            self.panel = tk.Label(
                self.windows,
                background='#202123',
                foreground='#202123'
            )

            self.panel.place(
                x=0,
                y=0,
                width=260,
                height=500
            )

            # // Logo / #

            self.Logo_img = PhotoImage(
                file=r'images\robot.png'
            )

            self.Logo = tk.Label(
                self.windows,
                image=self.Logo_img,
                background='#202123',
                foreground='#202123'
            )

            self.Logo.place(
                x=1,
                y=130
            )

            # // Conitunar / #

            self.continuer = tk.Button(
                self.windows,
                text='CONTINUAR',
                cursor='hand2',
                font=(
                    'Arial', 10
                ),
                background='#232a38',
                foreground='white',
                activeforeground='grey',
                activebackground='white',
                border=0,
                command=lambda: [
                    {
                        self._continuar_()
                    }
                ]
            )

            self.continuer.place(
                x=490,
                y=450
            )

            # // Cancelar / #

            self.cancelar = tk.Button(
                self.windows,
                text='CANCELAR',
                cursor='hand2',
                font=(
                    'Arial', 10
                ),
                background='#232a38',
                foreground='white',
                activeforeground='grey',
                activebackground='white',
                border=0,
                command=lambda: [
                    {
                        self._cancelar_()
                    }
                ]
            )

            self.cancelar.place(
                x=285,
                y=450
            )

            # // Information --> Scrollbar / #

            self.Texto = tk.Text(
                self.windows,
                background='#232a38',
                foreground='white',
                font=(
                    'Arial', 13
                ),
                border=0,
                state=NORMAL
            )

            self.Texto.insert(
                END,
                '\n  VERSION 1.0.0\n\n En estas version tendras que crearte \n una cuenta para poder continuar ya \n que en actualisaciones futuras \n pondremos una funcion la cual nos \n ayudara a mejorar el comportamiento \n de nuestro boot. \n\n Por parte de nuestro programador \n xRICKYTOx se les agradeceria en su \n colaboracion para el mejoramiento de \n diferentes funciones de nuestra app o \n aplicacion. \n\n En actulisaciones futuras agregaremos \n nuevas funciones las cuales \n mensionaremos en cada uno de los \n parches. \n\n Algunos ejemplos que les podras pedir \n al boot es que te pueda abrir diferentes \n aplicaciones asi como interactuar de \n manera simple. Por el momento \n tenemos muy limitada la informacion \n que esta implementada para este \n programa. \n\n Todos los derechos estan reservados \n por el desarrollador xRICKYTOx. \n\n ©Copyright 2023-2024 \n'
            )

            self.Texto.after(
                100, self._desactive_text_()
            )

            self.Srll = tk.Scrollbar(
                self.windows,
                command=self.Texto.yview,
                cursor='hand2'
            )

            self.Srll.place(
                x=570,
                y=10,
                width=20,
                height=415
            )

            self.Texto.place(
                x=270,
                y=10,
                width=300,
                height=415
            )

            self.Texto.config(
                yscrollcommand=self.Srll.set
            )

            self.windows.mainloop()

        def _desactive_text_(self):
            self.Texto.config(
                state=DISABLED
            )

        def _cancelar_(self):
            self.windows.withdraw()
            self.windows.destroy()
            exit()

        def _continuar_(self):
            self.windows.withdraw()
            return exe2()

    exe1()


class exe():
    def __init__(
            self
    ):
        windows.geometry(
            '600x500+650+290'
        )
        windows.resizable(
            False,
            False
        )
        windows.title(
            ''
        )
        windows.config(
            background='#232a38'
        )
        windows.iconbitmap(
            r'images\update.ico'
        )

        # // Panel / #

        self.panel = tk.Label(
            windows,
            background='#202123',
            foreground='#202123'
        )

        self.panel.place(
            x=0,
            y=0,
            width=260,
            height=500
        )

        # // Logo / #

        self.Logo_img = PhotoImage(
            file=r'images\robot.png'
        )

        self.Logo = tk.Label(
            windows,
            image=self.Logo_img,
            background='#202123',
            foreground='#202123'
        )

        self.Logo.place(
            x=1,
            y=130
        )

        # // Conitunar / #

        self.continuer = tk.Button(
            windows,
            text='CONTINUAR',
            cursor='hand2',
            font=(
                'Arial', 10
            ),
            background='#232a38',
            foreground='white',
            activeforeground='grey',
            activebackground='white',
            border=0,
            command=lambda: [
                {
                    self._continuar_()
                }
            ]
        )

        self.continuer.place(
            x=490,
            y=450
        )

        # // Cancelar / #

        self.cancelar = tk.Button(
            windows,
            text='CANCELAR',
            cursor='hand2',
            font=(
                'Arial', 10
            ),
            background='#232a38',
            foreground='white',
            activeforeground='grey',
            activebackground='white',
            border=0,
            command=lambda: [
                {
                    self._cancelar_()
                }
            ]
        )

        self.cancelar.place(
            x=285,
            y=450
        )

        # // Information --> Scrollbar / #

        self.Texto = tk.Text(
            windows,
            background='#232a38',
            foreground='white',
            font=(
                'Arial', 13
            ),
            border=0,
            state=NORMAL
        )

        self.Texto.insert(
            END,
            '\n  VERSION 1.0.0\n\n En estas version tendras que crearte \n una cuenta para poder continuar ya \n que en actualisaciones futuras \n pondremos una funcion la cual nos \n ayudara a mejorar el comportamiento \n de nuestro boot. \n\n Por parte de nuestro programador \n xRICKYTOx se les agradeceria en su \n colaboracion para el mejoramiento de \n diferentes funciones de nuestra app o \n aplicacion. \n\n En actulisaciones futuras agregaremos \n nuevas funciones las cuales \n mensionaremos en cada uno de los \n parches. \n\n Algunos ejemplos que les podras pedir \n al boot es que te pueda abrir diferentes \n aplicaciones asi como interactuar de \n manera simple. Por el momento \n tenemos muy limitada la informacion \n que esta implementada para este \n programa. \n\n Todos los derechos estan reservados \n por el desarrollador xRICKYTOx. \n\n ©Copyright 2023-2024 \n'
        )

        self.Texto.after(
            100, self._desactive_text_()
        )

        self.Srll = tk.Scrollbar(
            windows,
            command=self.Texto.yview,
            cursor='hand2'
        )

        self.Srll.place(
            x=570,
            y=10,
            width=20,
            height=415
        )

        self.Texto.place(
            x=270,
            y=10,
            width=300,
            height=415
        )

        self.Texto.config(
            yscrollcommand=self.Srll.set
        )

        windows.mainloop()

    def _desactive_text_(self):
        self.Texto.config(
            state=DISABLED
        )

    def _cancelar_(self):
        windows.withdraw()
        windows.destroy()
        exit()

    def _continuar_(self):
        windows.withdraw()
        return exe2()


exe()
