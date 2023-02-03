from tkinter import *
from tkinter import messagebox, PhotoImage
import subprocess
import os
import webbrowser

## // Chat Boot \\ ##

windows = Tk()


searchs = StringVar()


class chat_boot():

    def __init__(
            self
    ):
        # // Visual

        windows.config(
            background='#202123'
        )

        windows.attributes(
            '-fullscreen', True
        )

        # // Buscador

        self.search = Entry(
            windows,
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
            windows,
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
            windows,
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
            windows,
            background='#232a38',
            foreground='#232a38',
            padx=200,
            pady=1080
        )

        panel_izquierdo.place(
            x=-120,
            y=0
        )

        # // New Chat

        nuevo_chat = Button(
            windows,
            text='Chat Nuevo',
            background='#232a38',
            foreground='white',
            font=(
                'Arial Black', 15
            ),
            border=1,
            cursor='hand2',
            activebackground='#232a38',
            command=lambda: [
                {

                }
            ]
        )

        nuevo_chat.place(
            x=1685,
            y=100
        )

        # // Borrar Chat

        borrar_caht = Label(
            windows,
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
            file=r'App\Img\clear.png'
        )

        icon = Button(
            windows,
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
            windows,
            wrap=NONE,
            background='#202123',
            foreground='white',
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
            windows, command=self.Respuesta.yview, cursor='hand2'
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

        windows.bind(
            '<Escape>', self.exit_chat
        )

        windows.bind(
            '<Return>', self.buscador_funcion
        )

        windows.mainloop()

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
            print(
                exit()
            )

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
                    'C:/Riot Games/Riot Client/RiotClientServices.exe'
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


if __name__ == '__main__':
    chat_boot()
