"""Instalación del programa Chat Boot"""

from tkinter import Tk, Button, Label, Scrollbar, PhotoImage, Text, DISABLED, END, Toplevel, ttk
import time
import shutil
import subprocess
import win32api

windows = Tk()
name_pc = win32api.GetUserName()


class ExePantallaFinal():
    """Panel de despedida"""

    def __init__(
        self
    ):
        self.windows = Toplevel()
        self.windows.resizable(
            False,
            False
        )
        self.windows.geometry(
            '640x520+650+290'
        )
        self.windows.config(
            background='#232a38'
        )
        self.windows.iconbitmap(
            r'images\update.ico'
        )

        # Panel -> Izquierdo -> Logo

        panel = Label(
            self.windows,
            background='#202123'
        )

        panel.place(
            width=280,
            height=640,
            x=0,
            y=0
        )

        logo_img = PhotoImage(
            file=r'images\robot.png'
        )

        logo = Label(
            self.windows,
            image=logo_img,
            background='#202123'
        )

        logo.place(
            x=5,
            y=130
        )

        # Agradecimiento por instalar el programa

        agradecimiento = Label(
            self.windows,
            text='Muchas Gracias\npor instalar \nel programa !!!',
            background='#232a38',
            foreground='white',
            font=(
                'Arial Black', 25
            )
        )

        agradecimiento.place(
            x=310,
            y=125
        )

        # Boton -> Borde -> Instalar

        borde1_instalar = Label(
            self.windows,
            background='#232a38',
            foreground='white',
            text='__________'
        )

        borde1_instalar.place(
            x=554,
            y=456
        )

        borde2_instalar = Label(
            self.windows,
            background='#232a38',
            foreground='white',
            text='__________'
        )

        borde2_instalar.place(
            x=554,
            y=485
        )

        boton_instalar = Button(
            self.windows,
            text='SALIR',
            background='#232a38',
            foreground='white',
            activebackground='white',
            activeforeground='grey',
            font=(
                'Arial', 10
            ),
            border=0,
            cursor='hand2',
            command=lambda: [
                {
                    self.salir()
                }
            ]
        )

        boton_instalar.place(
            x=560,
            y=475
        )

        # Funciones -> Teclado

        self.windows.bind(
            '<Return>', lambda event: self.salir_teclado()
        )

        self.windows.mainloop()

    def mover_acceso_directo(self):
        """Mueve el archivo .link al escritorio"""
        folder = r'C:\CHAT-BOOT\CHAT-BOOT.lnk'
        destino = f'C:/Users/{name_pc}/OneDrive/Escritorio'
        shutil.move(
            folder, destino
        )

    def salir(self):
        """Salir de la instalación"""
        self.mover_acceso_directo()
        self.windows.destroy()
        windows.destroy()
        subprocess.Popen(
            [
                'taskkill',
                '/f',
                '/im',
                'INSTALL.exe'
            ]
        )

    def salir_teclado(self):
        """Salir de la instalación con una tecla"""
        self.mover_acceso_directo()
        self.windows.destroy()
        windows.destroy()
        subprocess.Popen(
            [
                'taskkill',
                '/f',
                '/im',
                'INSTALL.exe'
            ]
        )


class ExeInstalcionPag():
    """Panel de Instalación"""

    def __init__(
        self
    ):
        # Visual

        self.windows = Toplevel()
        self.windows.resizable(
            False,
            False
        )
        self.windows.geometry(
            '640x520+650+290'
        )
        self.windows.config(
            background='#232a38'
        )
        self.windows.iconbitmap(
            r'images\update.ico'
        )

        # Panel -> Izquierdo -> Logo

        panel = Label(
            self.windows,
            background='#202123'
        )

        panel.place(
            width=280,
            height=640,
            x=0,
            y=0
        )

        logo_img = PhotoImage(
            file=r'images\robot.png'
        )

        logo = Label(
            self.windows,
            image=logo_img,
            background='#202123'
        )

        logo.place(
            x=5,
            y=130
        )

        # Boton -> Borde -> Regresar
        borde1_regresar = Label(
            self.windows,
            background='#232a38',
            foreground='white',
            text='_________________'
        )

        borde1_regresar.place(
            x=305,
            y=456
        )

        borde2_regresar = Label(
            self.windows,
            background='#232a38',
            foreground='white',
            text='_________________'
        )

        borde2_regresar.place(
            x=305,
            y=485
        )

        self.boton_regresar = Button(
            self.windows,
            text='REGRESAR',
            background='#232a38',
            foreground='white',
            activebackground='white',
            activeforeground='grey',
            font=(
                'Arial', 10
            ),
            cursor='hand2',
            border=0,
            command=lambda: [
                {
                    self.regresar()
                }
            ]
        )

        self.boton_regresar.place(
            x=310,
            y=475
        )

        # Boton -> Borde -> Instalar

        borde1_instalar = Label(
            self.windows,
            background='#232a38',
            foreground='white',
            text='_______________'
        )

        borde1_instalar.place(
            x=544,
            y=456
        )

        borde2_instalar = Label(
            self.windows,
            background='#232a38',
            foreground='white',
            text='_______________'
        )

        borde2_instalar.place(
            x=544,
            y=485
        )

        boton_instalar = Button(
            self.windows,
            text='INSTALAR',
            background='#232a38',
            foreground='white',
            activebackground='white',
            activeforeground='grey',
            font=(
                'Arial', 10
            ),
            border=0,
            cursor='hand2',
            command=lambda: [
                {
                    self.instalar()
                }
            ]
        )

        boton_instalar.place(
            x=550,
            y=475
        )

        # Version de la Instalacion

        version = Label(
            self.windows,
            text='VER 1.0.1',
            background='#232a38',
            foreground='white',
            font=(
                'Arial Black', 30
            )
        )

        version.place(
            x=348,
            y=100
        )

        # Barra de instalación

        estilo = ttk.Style()

        estilo.theme_use('clam')

        estilo.configure(
            "TProgressbar",
            troughcolor='#202123',
            background='#2b79c2',
            bordercolor='#202123',
        )

        self.barra_instalacion = ttk.Progressbar(
            self.windows,
            style="TProgressbar",
            orient='horizontal',
            length=315
        )

        self.barra_instalacion.place(
            height=40,
            x=303,
            y=350
        )
        # Funciones -> Teclado

        self.windows.bind(
            '<Return>', lambda event: self.instalar()
        )

        self.windows.mainloop()

    def instalar(self):
        """Instalación del programa"""
        self.boton_regresar.config(
            state=DISABLED
        )
        task = 13
        porcentaje = 0
        while porcentaje < task:
            time.sleep(0.5)
            self.barra_instalacion['value'] += 13
            porcentaje += 1.3
            self.windows.update_idletasks()
        if porcentaje > task:
            self.mover_paquetes()

    def mover_paquetes(self):
        """Mueve el documento de la aplicación"""
        folder = r'CHAT-BOOT'
        destino = r'C:/'
        shutil.move(folder, destino)
        self.windows.withdraw()
        return ExePantallaFinal()

    def regresar(self):
        """Regresa al panel principal"""
        self.windows.destroy()
        windows.deiconify()
        ExePrincipalPag()


class ExePrincipalPag():
    """Pagina principal de la Instalcion"""

    def __init__(
        self
    ):
        # Visual

        windows.geometry(
            '640x520+650+290'
        )
        windows.title(
            ''
        )
        windows.config(
            background='#232a38'
        )
        windows.resizable(
            False,
            False
        )
        windows.iconbitmap(
            r'images\update.ico'
        )

        # Panel -> Izquierdo

        panel = Label(
            windows,
            background='#202123',
        )

        panel.place(
            width=280,
            height=640,
            x=0,
            y=0
        )

        # Logo

        logo_img = PhotoImage(
            file=r'images\robot.png'
        )

        logo = Label(
            windows,
            image=logo_img,
            background='#202123'
        )

        logo.place(
            x=5,
            y=130
        )

        # Condiciones --> Scrollbar

        self.condiciones = Text(
            windows,
            background='#232a38',
            foreground='white',
            font=(
                'Arial', 13
            ),
            width=35,
            height=23,
            border=0
        )

        scrollbar = Scrollbar(
            windows,
            command=self.condiciones.yview,
            cursor='hand2'
        )

        self.condiciones.insert(
            END,
            '\n  VERSION 1.0.1\n\n En estas version tendrás que crearte \n '
        )

        self.condiciones.insert(
            END,
            'una cuenta para poder continuar ya \n que en actualizaciones futuras \n '
        )

        self.condiciones.insert(
            END,
            'pondremos una funcion la cual nos \n ayudara a mejorar el comportamiento \n '
        )

        self.condiciones.insert(
            END,
            'de nuestro juego. \n\n Por parte del desarrollador \n xRICKYTOx, se les agradecería '
        )

        self.condiciones.insert(
            END,
            'en su \n colaboración para el mejoramiento de \n diferentes funciones '
        )

        self.condiciones.insert(
            END,
            'de nuestra app o \n aplicación. \n\n En actualizaciones futuras agregare- \n mos '
        )

        self.condiciones.insert(
            END,
            'nuevas funciones las cuales \n mencionaremos en cada uno de los \n parches.'
        )

        self.condiciones.insert(
            END,
            '\n\n Por el momento tenemos muy limitada \n la información y acciones que se \n '
        )

        self.condiciones.insert(
            END,
            'realizan al momento de querer dar una \n función al BOOT.'
        )

        self.condiciones.insert(
            END,
            '\n\n Todos los derechos están reservados \n por el desarrollador xRICKYTOx.'
        )

        self.condiciones.insert(
            END,
            '\n\n ©Copyright 2023-2024 \n'
        )

        self.condiciones.place(
            x=300,
            y=10
        )

        scrollbar.place(
            x=600,
            y=11,
            height=438,
            width=18
        )

        self.condiciones.config(
            yscrollcommand=scrollbar.set
        )

        self.condiciones.after(
            100, self.desactivar_condiciones()
        )

        # Boton -> Borde -> Continuar

        borde1_continuar = Label(
            windows,
            background='#232a38',
            foreground='white',
            text='_________________'
        )

        borde1_continuar.place(
            x=526,
            y=456
        )

        borde2_continuar = Label(
            windows,
            background='#232a38',
            foreground='white',
            text='_________________'
        )

        borde2_continuar.place(
            x=526,
            y=485
        )

        self.boton_continuar = Button(
            windows,
            text='CONTINUAR',
            background='#232a38',
            activebackground='white',
            foreground='white',
            activeforeground='grey',
            font=(
                'Arial', 10
            ),
            cursor='hand2',
            border=0,
            command=lambda: [
                {
                    self.continuar()
                }
            ]
        )

        self.boton_continuar.place(
            x=530,
            y=475
        )

        # Funciones -> Teclado

        windows.bind(
            '<Return>', lambda event: self.continuar()
        )

        windows.mainloop()

    def desactivar_condiciones(self):
        """Desactiva el campo de texto"""
        self.condiciones.config(
            state=DISABLED
        )

    def continuar(self):
        """Continua a la pagina de Instalcion"""
        windows.withdraw()
        ExeInstalcionPag()


ExePrincipalPag()
