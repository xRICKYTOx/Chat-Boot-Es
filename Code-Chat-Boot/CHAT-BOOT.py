from tkinter import *
from tkinter import messagebox, PhotoImage
import tkinter as tk
import subprocess
import os
import webbrowser
import shelve
import sqlite3

## // Chat Boot \\ ##

windows = Tk()
searchs = StringVar()
Username = StringVar()
Password = StringVar()
# // Name CHAT-BOOT \\ #


def chat_boot():
    class chat_boot():

        def __init__(
                self
        ):
            # // Visual
            self.windows = Toplevel()
            self.windows.config(
                background='#202123'
            )
            self.windows.title(
                'CHAT BOOT'
            )
            self.windows.iconbitmap(
                r'images\icon-app.ico'
            )
            self.windows.attributes(
                '-fullscreen', True
            )

            # // Buscador

            self.search = Entry(
                self.windows,
                textvariable=searchs,
                justify=CENTER,
                background='#202123',
                foreground='white',
                font=(
                    'Arial', 20
                ),
            )

            self.search.place(
                x=450,
                y=950,
                width=1000,
                height=50
            )

            # // Bienvenida

            welcome = Label(
                self.windows,
                text='BIENVENIDO!!',
                background='#202123',
                foreground='white',
                font=(
                    'Arial Black', 45
                )
            )

            welcome.place(
                x=725,
                y=50
            )

            # // Panel Derecho

            panel_derecho = Label(
                self.windows,
                background='#232a38',
                foreground='#232a38',
                padx=200,
                pady=1080
            )

            panel_derecho.place(
                x=1600,
                y=0
            )

            # // Panel Izquierdo

            panel_izquierdo = Label(
                self.windows,
                background='#232a38',
                foreground='#232a38',
                padx=200,
                pady=1080
            )

            panel_izquierdo.place(
                x=-120,
                y=0
            )

            # // Borrar Chat

            borrar_caht = Label(
                self.windows,
                text='ELIMINAR',
                font=(
                    'Arial Black', 15
                ),
                background='#232a38',
                foreground='white'
            )

            borrar_caht.place(
                x=1710,
                y=250
            )

            icon_borrar = PhotoImage(
                file=r'images\clear.png'
            )

            icon = Button(
                self.windows,
                image=icon_borrar,
                background='#232a38',
                activebackground='#232a38',
                foreground='#232a38',
                border=0,
                cursor='hand2',
                command=lambda: [
                    {
                        self.limpiar_chat()
                    }
                ]
            )

            icon.place(
                x=1745,
                y=300
            )

            # // self.Respuesta del Boot -> Scrollbar

            self.Respuesta = Text(
                self.windows,
                wrap=NONE,
                background='#202123',
                foreground='white',
                state=DISABLED,
                padx=59,
                pady=120,
                font=(
                    'Arial', 15
                )
            )

            self.Respuesta.place(
                x=450,
                y=150
            )

            Scrollbar_Funcion = Scrollbar(
                self.windows, command=self.Respuesta.yview, cursor='hand2'
            )

            Scrollbar_Funcion.place(
                x=1429,
                y=150,
                height=793,
                width=20
            )

            self.Respuesta.config(
                yscrollcommand=Scrollbar_Funcion.set
            )

            # // Funciones del Teclas

            self.windows.bind(
                '<Escape>', self.exit_chat
            )

            self.windows.bind(
                '<Return>', self.buscador_funcion
            )

            self.windows.mainloop()

        # // Eliminar Informacion

        def limpiar_chat(self):
            self.Respuesta.config(
                state=NORMAL
            )
            self.Respuesta.delete(
                1.0,
                END
            )
            self.Respuesta.config(
                state=DISABLED
            )

        # // Exit

        def exit_chat(self, event):
            messagebox.showinfo(
                'ATENCION!!', 'ESTAS CERRANDO LA APLICACION DE CHAT BOOT PRESIONA LA TECLA ENTER PARA CONTINUAR'
            )
            print(
                exit()
            )

        # // Busquedas

        def buscador_hola(self):
            self.Respuesta.insert(
                END,
                'BOOT:  Hola!!, Como estas amigo?....\n\n'
            )
            self.Respuesta.after(
                2100
            )
            self.Respuesta.config(
                state=DISABLED
            )

        def buscador_exit(self):
            def exit_funcion():
                windows.destroy()
                self.windows.destroy()
                subprocess.call(
                    [
                        "taskkill",
                        "/f",
                        "/im",
                        "CHAT-BOOT.exe"
                    ]
                )
                exit()

            info = self.Respuesta.insert(
                END,
                'BOOT:  Gracias por pasar un rato conmigo. Adios!!....\n\n'
            )
            infp = self.Respuesta.after(
                2100
            )
            self.Respuesta.after(
                2500, exit_funcion
            )
            self.Respuesta.config(
                state=DISABLED
            )

        def buscador_open_block_notas(self):
            def block_notas():
                subprocess.Popen(
                    [
                        'notepad.exe'
                    ],
                    start_new_session=True
                )

            info = self.Respuesta.insert(
                END,
                'BOOT:  Abriendo un block de notas....\n\n'
            )
            info = self.Respuesta.after(
                2100
            )
            self.Respuesta.after(
                2300,
                block_notas
            )
            self.Respuesta.config(
                state=DISABLED
            )

        def buscador_close_block_notas(self):
            def block_notas():
                subprocess.Popen(
                    [
                        'taskkill',
                        '/f',
                        '/im',
                        'notepad.exe'
                    ]
                )

            info = self.Respuesta.insert(
                END,
                'BOOT:  Abriendo un block de notas....\n\n'
            )
            info = self.Respuesta.after(
                2100
            )
            self.Respuesta.after(
                2200,
                block_notas
            )
            self.Respuesta.config(
                state=DISABLED
            )

        def buscador_open_calculadora(self):
            def calculadora():
                os.system(
                    'start calc'
                )

            info = self.Respuesta.insert(
                END,
                'BOOT:  Abriendo la calculadora...\n\n'
            )
            info = self.Respuesta.after(
                2100
            )
            self.Respuesta.after(
                2200,
                calculadora
            )
            self.Respuesta.config(
                state=DISABLED
            )

        def buscador_close_calculadora(self):
            def calculadora():
                subprocess.Popen(
                    [
                        'taskkill',
                        '/f',
                        '/im',
                        'CalculatorApp.exe'
                    ]
                )

            info = self.Respuesta.insert(
                END,
                'BOOT:  Cerrando la calculadora....\n\n'
            )
            info = self.Respuesta.after(
                2100
            )
            self.Respuesta.after(
                2200,
                calculadora
            )
            self.Respuesta.config(
                state=DISABLED
            )

        def buscador_open_navegador(self):
            def navegador():
                webbrowser.open(
                    'https://www.google.com.mx/'
                )

            info = self.Respuesta.insert(
                END,
                'BOOT:  Abriendo el navegador...\n\n'
            )
            info = self.Respuesta.after(
                2100
            )
            self.Respuesta.after(
                2200,
                navegador
            )
            self.Respuesta.config(
                state=DISABLED
            )

        def buscador_close_navegador(self):
            def navegador():
                subprocess.call(
                    [
                        "taskkill",
                        "/f",
                        "/im",
                        "msedge.exe"
                    ]
                )
                subprocess.call(
                    [
                        "taskkill",
                        "/f",
                        "/im",
                        "brave.exe"
                    ]
                )
                subprocess.call(
                    [
                        "taskkill",
                        "/f",
                        "/im",
                        "chrome.exe"
                    ]
                )
                subprocess.call(
                    [
                        "taskkill",
                        "/f",
                        "/im",
                        "opera.exe"
                    ]
                )
                subprocess.call(
                    [
                        "taskkill",
                        "/f",
                        "/im",
                        "firefox.exe"
                    ]
                )

            info = self.Respuesta.insert(
                END,
                'BOOT:  Cerrando el navegador...\n\n'
            )
            info = self.Respuesta.after(
                2100
            )
            self.Respuesta.after(
                2200,
                navegador
            )
            self.Respuesta.config(
                state=DISABLED
            )

        def buscador_open_youtube(self):
            def navegador():
                webbrowser.open(
                    'https://www.youtube.com/'
                )

            info = self.Respuesta.insert(
                END,
                'BOOT:  Abriendo YouTube...\n\n'
            )
            info = self.Respuesta.after(
                2100
            )
            self.Respuesta.after(
                2200,
                navegador
            )
            self.Respuesta.config(
                state=DISABLED
            )

        def buscador_open_aplicacion_musica(self):
            def musica():
                subprocess.Popen(
                    [
                        'iTunes.exe'
                    ],
                    start_new_session=True
                )
            info = self.Respuesta.insert(
                END,
                'BOOT:  Abriendo iTunes...\n\n'
            )
            info = self.Respuesta.after(
                2100
            )
            self.Respuesta.after(
                2200,
                musica
            )
            self.Respuesta.config(
                state=DISABLED
            )

        def buscador_close_aplicacion_musica(self):
            def musica():
                subprocess.Popen(
                    [
                        'taskkill',
                        '/f',
                        '/im',
                        'iTunes.exe'
                    ]
                )
            info = self.Respuesta.insert(
                END,
                'BOOT:  Cerrando iTunes...\n\n'
            )
            info = self.Respuesta.after(
                2100
            )
            self.Respuesta.after(
                2200,
                musica
            )
            self.Respuesta.config(
                state=DISABLED
            )

        def buscador_open_explorador_archivos(self):
            def archivos():
                subprocess.Popen(
                    [
                        'explorer.exe'
                    ],
                    start_new_session=True
                )
            info = self.Respuesta.insert(
                END,
                'BOOT:  Abriendo el Explorador de Archivos...\n\n'
            )
            info = self.Respuesta.after(
                2100
            )
            self.Respuesta.after(
                2200,
                archivos
            )
            self.Respuesta.config(
                state=DISABLED
            )

        def buscador_open_riot_games(self):
            def riot():
                subprocess.Popen(
                    [
                        'RiotClientServices.exe'
                    ]
                )
            info = self.Respuesta.insert(
                END,
                'BOOT:  Abriendo Riot Games...\n\n'
            )
            info = self.Respuesta.after(
                2100
            )
            self.Respuesta.after(
                2200,
                riot
            )
            self.Respuesta.config(
                state=DISABLED
            )

        def buscador_close_riot_games(self):
            def riot():
                subprocess.Popen(
                    [
                        'taskkill',
                        '/f',
                        '/im',
                        'RiotClientServices.exe'
                    ]
                )

            info = self.Respuesta.insert(
                END,
                'BOOT:  Cerrando Riot Games...\n\n'
            )
            info = self.Respuesta.after(
                2100
            )
            self.Respuesta.after(
                2200,
                riot
            )
            self.Respuesta.config(
                state=DISABLED
            )

        def buscador_open_vsc(self):
            def vsc():
                os.system(
                    'Code'
                )

            info = self.Respuesta.insert(
                END,
                'BOOT:  Abriendo Visual Studio Code...\n\n'
            )
            info = self.Respuesta.after(
                2100
            )
            self.Respuesta.after(
                2200,
                vsc
            )
            self.Respuesta.config(
                state=DISABLED
            )

        def buscador_close_vsc(self):
            def vsc():
                subprocess.Popen(
                    [
                        'taskkill',
                        '/f',
                        '/im',
                        'Code.exe'
                    ]
                )

            info = self.Respuesta.insert(
                END,
                'BOOT:  Cerrando Visual Studio Code...\n\n'
            )
            info = self.Respuesta.after(
                2100
            )
            self.Respuesta.after(
                2200,
                vsc
            )
            self.Respuesta.config(
                state=DISABLED
            )

        def buscador_open_taskmgr(self):
            def taskmgr():
                subprocess.Popen(
                    [
                        'Taskmgr.exe'
                    ]
                )
            info = self.Respuesta.insert(
                END,
                'BOOT:  Abriendo el Administrador de Tareas...\n\n'
            )
            info = self.Respuesta.after(
                2100
            )
            self.Respuesta.after(
                2200,
                taskmgr
            )
            self.Respuesta.config(
                state=DISABLED
            )

        def buscador_close_taskmgr(self):
            def taskmgr():
                subprocess.Popen(
                    [
                        'taskkill',
                        '/f',
                        '/im',
                        'Taskmgr.exe'
                    ]
                )
            info = self.Respuesta.insert(
                END,
                'BOOT:  Abriendo el Administrador de Tareas...\n\n'
            )
            info = self.Respuesta.after(
                2100
            )
            self.Respuesta.after(
                2200,
                taskmgr
            )
            self.Respuesta.config(
                state=DISABLED
            )

        # // Busqueda de Informacion

        def buscador_funcion(self, event):

            busqueda = searchs.get()

            # // Resultados de Busqueda

            if busqueda == 'hola':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.Respuesta.after(
                    200,
                    self.buscador_hola
                )
                self.search.delete(
                    0,
                    END
                )
            elif busqueda == 'Hola':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.Respuesta.after(
                    200,
                    self.buscador_hola
                )
                self.search.delete(
                    0,
                    END
                )
            elif busqueda == 'HOLA':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.Respuesta.after(
                    200,
                    self.buscador_hola
                )
                self.search.delete(
                    0,
                    END
                )
            elif busqueda == 'exit':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.Respuesta.after(
                    200,
                    self.buscador_exit
                )
                self.search.delete(
                    0,
                    END
                )
            elif busqueda == 'Exit':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.Respuesta.after(
                    200,
                    self.buscador_exit
                )
                self.search.delete(
                    0,
                    END
                )
            elif busqueda == 'EXIT':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.Respuesta.after(
                    200,
                    self.buscador_exit
                )
                self.search.delete(
                    0,
                    END
                )
            elif busqueda == 'abre un block de notas':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_block_notas
                )
            elif busqueda == 'Abre un block de notas':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_block_notas
                )
            elif busqueda == 'ABRE UN BLOCK DE NOTAS':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_block_notas
                )
            elif busqueda == 'cierra el block de notas':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_close_block_notas
                )
            elif busqueda == 'Cierra el block de notas':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_close_block_notas
                )
            elif busqueda == 'CIERRA EL BLOCK DE NOTAS':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_close_block_notas
                )
            elif busqueda == 'abre la calculadora':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_calculadora
                )
            elif busqueda == 'Abre la calculadora':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_calculadora
                )
            elif busqueda == 'ABRE LA CALCULADORA':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_calculadora
                )
            elif busqueda == 'cierra la calculadora':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_close_calculadora
                )
            elif busqueda == 'Cierra la calculadora':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_close_calculadora
                )
            elif busqueda == 'CIERRA LA CALCULADORA':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_close_calculadora
                )
            elif busqueda == 'abre el navegador':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_navegador
                )
            elif busqueda == 'Abre el navegador':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_navegador
                )
            elif busqueda == 'ABRE EL NAVEGADOR':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_navegador
                )
            elif busqueda == 'cierra el navegador':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_close_navegador
                )
            elif busqueda == 'Cierra el navegador':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_close_navegador
                )
            elif busqueda == 'CIERRA EL NAVEGADOR':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_close_navegador
                )
            elif busqueda == 'abre youtube':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_youtube
                )
            elif busqueda == 'Abre youtube':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_youtube
                )
            elif busqueda == 'ABRE YOUTUBE':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_youtube
                )
            elif busqueda == 'abre yt':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_youtube
                )
            elif busqueda == 'Abre yt':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_youtube
                )
            elif busqueda == 'ABRE YT':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_youtube
                )
            elif busqueda == 'abre mi aplicacion de musica':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_aplicacion_musica
                )
            elif busqueda == 'Abre mi aplicacion de musica':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_aplicacion_musica
                )
            elif busqueda == 'ABRE MI APLICACION DE MUSICA':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_aplicacion_musica
                )
            elif busqueda == 'abre itunes':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_aplicacion_musica
                )
            elif busqueda == 'Abre itunes':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_aplicacion_musica
                )
            elif busqueda == 'ABRE ITUNES':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_aplicacion_musica
                )
            elif busqueda == 'cierra mi aplicacion de musica':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_close_aplicacion_musica
                )
            elif busqueda == 'Cierra mi aplicacion de musica':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_close_aplicacion_musica
                )
            elif busqueda == 'CIERRA MI APLICACION DE MUSICA':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_close_aplicacion_musica
                )
            elif busqueda == 'cierra itunes':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_close_aplicacion_musica
                )
            elif busqueda == 'Cierra itunes':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_close_aplicacion_musica
                )
            elif busqueda == 'CIERRA ITUNES':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_close_aplicacion_musica
                )
            elif busqueda == 'abre el explorador de archivos':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_explorador_archivos
                )
            elif busqueda == 'Abre el explorador de archivos':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_explorador_archivos
                )
            elif busqueda == 'ABRE EL EXPLORADOR DE ARCHIVOS':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_explorador_archivos
                )
            elif busqueda == 'abre riot games':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_riot_games
                )
            elif busqueda == 'Abre riot games':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_riot_games
                )
            elif busqueda == 'ABRE RIOT GAMES':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_riot_games
                )
            elif busqueda == 'cierra riot games':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_close_riot_games
                )
            elif busqueda == 'Cierra riot games':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_close_riot_games
                )
            elif busqueda == 'CIERRA RIOT GAMES':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_close_riot_games
                )
            elif busqueda == 'abre visual studio code':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_vsc
                )
            elif busqueda == 'Abre visual studio code':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_vsc
                )
            elif busqueda == 'ABRE VISUAL STUDIO CODE':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_vsc
                )
            elif busqueda == 'abre vsc':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_vsc
                )
            elif busqueda == 'Abre vsc':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_vsc
                )
            elif busqueda == 'ABRE VSC':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_vsc
                )
            elif busqueda == 'cierra visual studio code':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_close_vsc
                )
            elif busqueda == 'Cierra visual studio code':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_close_vsc
                )
            elif busqueda == 'CIERRA VISUAL STUDIO CODE':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_close_vsc
                )
            elif busqueda == 'cierra vsc':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_close_vsc
                )
            elif busqueda == 'Cierra vsc':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_close_vsc
                )
            elif busqueda == 'CIERRA VSC':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_close_vsc
                )
            elif busqueda == 'abre el administrador de tareas':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_taskmgr
                )
            elif busqueda == 'Abre el administrador de tareas':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_taskmgr
                )
            elif busqueda == 'ABRE EL ADMINISTRADOR DE TAREAS':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_open_taskmgr
                )
            elif busqueda == 'cierra el administrador de tareas':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_close_taskmgr
                )
            elif busqueda == 'Cierra el administrador de tareas':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_close_taskmgr
                )
            elif busqueda == 'CIERRA EL ADMINISTRADOR DE TAREAS':
                self.Respuesta.config(
                    state=NORMAL
                )
                self.Respuesta.insert(
                    END,
                    f'YO:  {searchs.get()}\n\n'
                )
                self.search.delete(
                    0,
                    END
                )
                self.Respuesta.after(
                    200, self.buscador_close_taskmgr
                )
            else:
                messagebox.showerror(
                    'ERROR', f'LA PALABRA {searchs.get()} NO ESTA VINCULADA AL CHAT BOOT'
                )

    chat_boot()


def log_in():

    class login():
        def __init__(
            self
        ):
            self.windows = Toplevel()
            self.windows.geometry(
                '1000x600+425+245'
            )
            self.windows.resizable(
                False, False
            )
            self.windows.title(
                ''
            )
            self.windows.iconbitmap(
                r'images\icon-user.ico'
            )
            self.windows.config(
                background='#202123'
            )

            # // Panel Log In \\ #

            self.Panel_log_in = tk.Label(
                self.windows,
                background='#232a38'
            )

            self.Panel_log_in.place(
                x=0,
                y=0,
                width=400,
                height=600
            )

            # // Logo \\ #
            self.Log_img = PhotoImage(
                file=r'images\logo-robot.png'
            )

            self.Log = tk.Label(
                self.windows,
                image=self.Log_img,
                background='#202123',
                foreground='#202123'
            )

            self.Log.place(
                x=443,
                y=53
            )

            # // Log In \\ #

            self.Log_in_txt = tk.Label(
                self.windows,
                text='Log In',
                font=(
                    'Arial Black', 40
                ),
                background='#232a38',
                foreground='white'
            )

            self.Log_in_txt.place(
                x=105,
                y=30
            )

            self.Log_in_entry_username_txt = tk.Label(
                self.windows,
                text='Username',
                font=(
                    'Arial', 18
                ),
                background='#232a38',
                foreground='white'
            )

            self.Log_in_entry_username_txt.place(
                x=50,
                y=150
            )

            self.Log_in_entry_username = tk.Entry(
                self.windows,
                textvariable=Username,
                font=(
                    'Arial', 18
                ),
                background='#202123',
                foreground='white',
                justify=CENTER
            )

            self.Log_in_entry_username.place(
                x=50,
                y=190,
                width=300
            )
            self.Log_in_entry_username.delete(
                0,
                END
            )
            self.Log_in_entry_password_txt = tk.Label(
                self.windows,
                text='Password',
                font=(
                    'Arial', 18
                ),
                background='#232a38',
                foreground='white'
            )

            self.Log_in_entry_password_txt.place(
                x=50,
                y=250
            )

            self.Log_in_entry_password = tk.Entry(
                self.windows,
                textvariable=Password,
                font=(
                    'Arial', 18
                ),
                background='#202123',
                foreground='white',
                justify=CENTER,
                show=(
                    '*'
                )
            )

            self.Log_in_entry_password.place(
                x=50,
                y=290,
                width=300
            )

            self.Log_in_entry_password.delete(
                0,
                END
            )

            # // Notview Password \\ #

            self.not_view_password_txt = tk.Label(
                self.windows,
                text='View Password',
                background='#232a38',
                foreground='white',
                font=(
                    'Arial', 14
                )
            )

            self.not_view_password_txt.place(
                x=100,
                y=343
            )

            self.not_view_password = tk.Button(
                self.windows,
                background='white',
                foreground='white',
                cursor='hand2',
                activebackground='grey',
                activeforeground='grey',
                command=lambda: [
                    {
                        self.view_password()
                    }
                ],
                border=0
            )

            self.not_view_password.place(
                x=70,
                y=350,
                width=15,
                height=15
            )

            # // Log In Button \\ #

            self.button_log_in = tk.Button(
                self.windows,
                text='LOG IN',
                font=(
                    'Arial Black', 14
                ),
                background='#202123',
                activebackground='white',
                foreground='white',
                activeforeground='grey',
                cursor='hand2',
                command=lambda: self.log_in_(
                    Username.get(), Password.get()
                )
            )

            self.button_log_in.place(
                x=50,
                y=430,
                width=300
            )

            self.button_sign_up = tk.Button(
                self.windows,
                text='SIGN UP',
                font=(
                    'Arial Black', 14
                ),
                background='white',
                activebackground='#202123',
                foreground='grey',
                activeforeground='white',
                cursor='hand2',
                command=lambda: [
                    {
                        self.sign_up_()
                    }
                ]
            )

            self.button_sign_up.place(
                x=50,
                y=500,
                width=300
            )
            self.windows.mainloop()

        def sign_up_(self):
            self.windows.withdraw()
            self.Log_in_entry_username.delete(
                0, END
            )
            self.Log_in_entry_password.delete(
                0, END
            )
            return sign_up()

        def view_password(self):
            self.Log_in_entry_password.config(
                show=(
                    ''
                )
            )
            view_password = tk.Button(
                self.windows,
                background='grey',
                foreground='grey',
                cursor='hand2',
                activebackground='white',
                activeforeground='white',
                command=lambda: [
                    {
                        self.not_view_password_()
                    }
                ],
                border=0
            )

            view_password.place(
                x=70,
                y=350,
                width=15,
                height=15
            )

        def not_view_password_(self):
            self.Log_in_entry_password.config(
                show=(
                    '*'
                )
            )
            not_view_password = tk.Button(
                self.windows,
                background='white',
                foreground='white',
                cursor='hand2',
                activebackground='grey',
                activeforeground='grey',
                command=lambda: [
                    {
                        self.view_password()
                    }
                ],
                border=0
            )

            not_view_password.place(
                x=70,
                y=350,
                width=15,
                height=15
            )

        def log_in_(self, username, password):
            connect = sqlite3.connect(
                r'users_passwords.db'
            )
            cursor = connect.cursor()

            cursor.execute(
                "SELECT * FROM user_password WHERE Username = ? AND Password = ?", (
                    username, password)
            )
            result = cursor.fetchall()
            if result:
                messagebox.showinfo(
                    "LOGIN", f"Has iniciado sesion correctamente con el usuario [{Username.get()}]"
                )
                self.windows.withdraw()
                return chat_boot()
            else:
                messagebox.showerror(
                    "LOGIN", f"El usuario [{Username.get()}] o la contraña son incorrectos."
                )
                self.Log_in_entry_username.delete(
                    0, END
                )
                self.Log_in_entry_password.delete(
                    0, END
                )
                return self.not_view_password_()

    login()


def sign_up():

    class sign_up():
        def __init__(
            self
        ):
            self.windows = Toplevel()
            self.windows.geometry(
                '1000x600+425+245'
            )
            self.windows.resizable(
                False, False
            )
            self.windows.title(
                ''
            )
            self.windows.iconbitmap(
                r'images\icon-user.ico'
            )
            self.windows.config(
                background='#202123'
            )

            # // Panel Log In \\ #

            self.Panel_log_in = tk.Label(
                self.windows,
                background='#232a38'
            )

            self.Panel_log_in.place(
                x=0,
                y=0,
                width=400,
                height=600
            )

            # // Logo \\ #
            self.Log_img = PhotoImage(
                file=r'images\logo-robot.png'
            )

            self.Log = tk.Label(
                self.windows,
                image=self.Log_img,
                background='#202123',
                foreground='#202123'
            )

            self.Log.place(
                x=443,
                y=53
            )

            # // Sign Up \\ #

            self.Log_in_txt = tk.Label(
                self.windows,
                text='Sign Up',
                font=(
                    'Arial Black', 40
                ),
                background='#232a38',
                foreground='white'
            )

            self.Log_in_txt.place(
                x=85,
                y=30
            )

            self.Log_in_entry_username_txt = tk.Label(
                self.windows,
                text='Username',
                font=(
                    'Arial', 18
                ),
                background='#232a38',
                foreground='white'
            )

            self.Log_in_entry_username_txt.place(
                x=50,
                y=150
            )

            self.Log_in_entry_username = tk.Entry(
                self.windows,
                textvariable=Username,
                font=(
                    'Arial', 18
                ),
                background='#202123',
                foreground='white',
                justify=CENTER
            )

            self.Log_in_entry_username.place(
                x=50,
                y=190,
                width=300
            )

            self.Log_in_entry_password_txt = tk.Label(
                self.windows,
                text='Password',
                font=(
                    'Arial', 18
                ),
                background='#232a38',
                foreground='white'
            )

            self.Log_in_entry_password_txt.place(
                x=50,
                y=250
            )

            self.Log_in_entry_password = tk.Entry(
                self.windows,
                textvariable=Password,
                font=(
                    'Arial', 18
                ),
                background='#202123',
                foreground='white',
                justify=CENTER,
                show=(
                    '*'
                )
            )

            self.Log_in_entry_password.place(
                x=50,
                y=290,
                width=300
            )

            # // Notview Password \\ #

            self.not_view_password_txt = tk.Label(
                self.windows,
                text='View Password',
                background='#232a38',
                foreground='white',
                font=(
                    'Arial', 14
                )
            )

            self.not_view_password_txt.place(
                x=100,
                y=343
            )

            self.not_view_password = tk.Button(
                self.windows,
                background='white',
                foreground='white',
                cursor='hand2',
                activebackground='grey',
                activeforeground='grey',
                command=lambda: [
                    {
                        self.view_password()
                    }
                ],
                border=0
            )

            self.not_view_password.place(
                x=70,
                y=350,
                width=15,
                height=15
            )

            # // Log In Button \\ #

            self.button_log_in = tk.Button(
                self.windows,
                text='LOG IN',
                font=(
                    'Arial Black', 14
                ),
                background='#202123',
                activebackground='white',
                foreground='white',
                activeforeground='grey',
                cursor='hand2',
                command=lambda: [
                    {
                        self.log_in_()
                    }
                ]
            )

            self.button_log_in.place(
                x=50,
                y=500,
                width=300
            )

            self.button_sign_up = tk.Button(
                self.windows,
                text='SIGN UP',
                font=(
                    'Arial Black', 14
                ),
                background='white',
                activebackground='#202123',
                foreground='grey',
                activeforeground='white',
                cursor='hand2',
                command=lambda: self.sign_up_(
                    Username.get(), Password.get()
                )
            )

            self.button_sign_up.place(
                x=50,
                y=430,
                width=300
            )
            self.windows.mainloop()

        def log_in_(self):
            self.windows.withdraw()
            self.Log_in_entry_username.delete(
                0, END
            )
            self.Log_in_entry_password.delete(
                0, END
            )
            return log_in()

        def sign_up_(self, username, password):

            conection = sqlite3.connect(
                r'users_passwords.db'
            )
            cursor = conection.cursor()
            cursor.execute(
                "SELECT * FROM user_password WHERE Username = ? AND Password = ?", (username, password))
            result = cursor.fetchall()

            if result:
                messagebox.showerror(
                    'ERROR', f'El usuario [{Username.get()}] ya esta registrado en esta aplicacion. Porfavor inicia sesion.'
                )
                self.Log_in_entry_username.delete(
                    0,
                    END
                )
                self.Log_in_entry_password.delete(
                    0,
                    END
                )
                self.windows.destroy()
                return log_in()
            else:
                messagebox.showinfo(
                    'CONGRATULATIONS', f'Felicidades el usuario [{Username.get()}] se a registrado con exito!!!'
                )
                cursor.execute(
                    f"INSERT INTO user_password VALUES ('{Username.get()}','{Password.get()}')"
                )
                conection.commit()
                cursor.close()
                self.Log_in_entry_username.delete(
                    0,
                    END
                )
                self.Log_in_entry_password.delete(
                    0,
                    END
                )
                self.windows.withdraw()
                return log_in()

        def view_password(self):
            self.Log_in_entry_password.config(
                show=(
                    ''
                )
            )
            view_password = tk.Button(
                self.windows,
                background='grey',
                foreground='grey',
                cursor='hand2',
                activebackground='white',
                activeforeground='white',
                command=lambda: [
                    {
                        self.not_view_password_()
                    }
                ],
                border=0
            )

            view_password.place(
                x=70,
                y=350,
                width=15,
                height=15
            )

        def not_view_password_(self):
            self.Log_in_entry_password.config(
                show=(
                    '*'
                )
            )
            not_view_password = tk.Button(
                self.windows,
                background='white',
                foreground='white',
                cursor='hand2',
                activebackground='grey',
                activeforeground='grey',
                command=lambda: [
                    {
                        self.view_password()
                    }
                ],
                border=0
            )

            not_view_password.place(
                x=70,
                y=350,
                width=15,
                height=15
            )

    sign_up()


class login():
    def __init__(
        self
    ):
        windows.geometry(
            '1000x600+425+245'
        )
        windows.resizable(
            False, False
        )
        windows.title(
            ''
        )
        windows.iconbitmap(
            r'images\icon-user.ico'
        )
        windows.config(
            background='#202123'
        )

        # // Panel Log In \\ #

        self.Panel_log_in = tk.Label(
            windows,
            background='#232a38'
        )

        self.Panel_log_in.place(
            x=0,
            y=0,
            width=400,
            height=600
        )

        # // Logo \\ #
        self.Log_img = PhotoImage(
            file=r'images\logo-robot.png'
        )

        self.Log = tk.Label(
            windows,
            image=self.Log_img,
            background='#202123',
            foreground='#202123'
        )

        self.Log.place(
            x=443,
            y=53
        )

        # // Log In \\ #

        self.Log_in_txt = tk.Label(
            windows,
            text='Log In',
            font=(
                'Arial Black', 40
            ),
            background='#232a38',
            foreground='white'
        )

        self.Log_in_txt.place(
            x=105,
            y=30
        )

        self.Log_in_entry_username_txt = tk.Label(
            windows,
            text='Username',
            font=(
                'Arial', 18
            ),
            background='#232a38',
            foreground='white'
        )

        self.Log_in_entry_username_txt.place(
            x=50,
            y=150
        )

        self.Log_in_entry_username = tk.Entry(
            windows,
            textvariable=Username,
            font=(
                'Arial', 18
            ),
            background='#202123',
            foreground='white',
            justify=CENTER
        )

        self.Log_in_entry_username.place(
            x=50,
            y=190,
            width=300
        )

        self.Log_in_entry_password_txt = tk.Label(
            windows,
            text='Password',
            font=(
                'Arial', 18
            ),
            background='#232a38',
            foreground='white'
        )

        self.Log_in_entry_password_txt.place(
            x=50,
            y=250
        )

        self.Log_in_entry_password = tk.Entry(
            windows,
            textvariable=Password,
            font=(
                'Arial', 18
            ),
            background='#202123',
            foreground='white',
            justify=CENTER,
            show=(
                '*'
            )
        )

        self.Log_in_entry_password.place(
            x=50,
            y=290,
            width=300
        )

        # // Notview Password \\ #

        self.not_view_password_txt = tk.Label(
            windows,
            text='View Password',
            background='#232a38',
            foreground='white',
            font=(
                'Arial', 14
            )
        )

        self.not_view_password_txt.place(
            x=100,
            y=343
        )

        self.not_view_password = tk.Button(
            windows,
            background='white',
            foreground='white',
            cursor='hand2',
            activebackground='grey',
            activeforeground='grey',
            command=lambda: [
                {
                    self.view_password()
                }
            ],
            border=0
        )

        self.not_view_password.place(
            x=70,
            y=350,
            width=15,
            height=15
        )

        # // Log In Button \\ #

        self.button_log_in = tk.Button(
            windows,
            text='LOG IN',
            font=(
                'Arial Black', 14
            ),
            background='#202123',
            activebackground='white',
            foreground='white',
            activeforeground='grey',
            cursor='hand2',
            command=lambda: self.log_in_(
                Username.get(), Password.get()
            )
        )

        self.button_log_in.place(
            x=50,
            y=430,
            width=300
        )

        self.button_sign_up = tk.Button(
            windows,
            text='SIGN UP',
            font=(
                'Arial Black', 14
            ),
            background='white',
            activebackground='#202123',
            foreground='grey',
            activeforeground='white',
            cursor='hand2',
            command=lambda: [
                {
                    self.sign_up_()
                }
            ]
        )

        self.button_sign_up.place(
            x=50,
            y=500,
            width=300
        )
        windows.mainloop()

    def sign_up_(self):
        windows.withdraw()
        self.Log_in_entry_username.delete(
            0, END
        )
        self.Log_in_entry_password.delete(
            0, END
        )
        return sign_up()

    def view_password(self):
        self.Log_in_entry_password.config(
            show=(
                ''
            )
        )
        view_password = tk.Button(
            windows,
            background='grey',
            foreground='grey',
            cursor='hand2',
            activebackground='white',
            activeforeground='white',
            command=lambda: [
                {
                    self.not_view_password_()
                }
            ],
            border=0
        )

        view_password.place(
            x=70,
            y=350,
            width=15,
            height=15
        )

    def not_view_password_(self):
        self.Log_in_entry_password.config(
            show=(
                '*'
            )
        )
        not_view_password = tk.Button(
            windows,
            background='white',
            foreground='white',
            cursor='hand2',
            activebackground='grey',
            activeforeground='grey',
            command=lambda: [
                {
                    self.view_password()
                }
            ],
            border=0
        )

        not_view_password.place(
            x=70,
            y=350,
            width=15,
            height=15
        )

    def log_in_(self, username, password):
        connect = sqlite3.connect(
            r'users_passwords.db'
        )
        cursor = connect.cursor()

        cursor.execute(
            "SELECT * FROM user_password WHERE Username = ? AND Password = ?", (
                username, password)
        )
        result = cursor.fetchall()
        if result:
            messagebox.showinfo(
                "LOGIN", f"Has iniciado sesion correctamente con el usuario [{Username.get()}]"
            )
            windows.withdraw()
            return chat_boot()
        else:
            messagebox.showerror(
                "LOGIN", f"El usuario [{Username.get()}] o la contraña son incorrectos."
            )
            self.Log_in_entry_username.delete(
                0, END
            )
            self.Log_in_entry_password.delete(
                0, END
            )
            return self.not_view_password_()


login()
