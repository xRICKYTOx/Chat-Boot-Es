"""Chat Boot"""

from tkinter import Toplevel, Label, StringVar, Button, Entry, Text, PhotoImage, Scrollbar, END

from Log.inicio_sesion_registrarme import Username, windows, messagebox

from Palabras.palabras_clave import *

from System.systema import *

from Web.internet import *


ventana = Toplevel()
Searches = StringVar()



# Función -> Activar -> Desactivar -> Salir -> Borrar-Chat


def activar_entry_desactivar_text():
    """Activa la entrada de texto -> Desactiva el Text"""
    buscador.config(
        state='normal'
    )
    respuesta.config(
        state='disabled'
    )


def salir_app():
    """Cierra la aplicación por completo"""
    windows.destroy()
    ventana.destroy()
    terminar_app()


def borrar_chat():
    respuesta.config(
        state='normal'
    )
    respuesta.delete(
        1.0,
        END
    )
    respuesta.config(
        state='disabled'
    )


# Funciones


def user_saludar(clave):
    """Saluda al usuario"""
    def saludar_usuario():
        respuesta.insert(
            END,
            f'BOOT:  Hola {Username.get()}!!, en que te puedo ayudar el día de hoy...?\n\n'
        )
        respuesta.after(
            200, activar_entry_desactivar_text
        )
    buscador.delete(
        0,
        END
    )
    respuesta.config(
        state='normal'
    )
    buscador.config(
        state='disabled',
        disabledbackground='#202123'
    )
    respuesta.insert(
        END,
        f'YO:  {clave}\n\n'
    )
    respuesta.after(
        2100, saludar_usuario
    )


def user_salir(clave):
    """Salir de la aplicación"""
    def despedir_usuario():
        respuesta.insert(
            END,
            f'BOOT:  Gracias {Username.get()}!!, por pasar un rato conmigo..\n\n'
        )
        respuesta.after(
            200, salir_app
        )
    buscador.delete(
        0,
        END
    )
    respuesta.config(
        state='normal'
    )
    buscador.config(
        state='disabled',
        disabledbackground='#202123'
    )
    respuesta.insert(
        END,
        f'YO:  {clave}\n\n'
    )
    respuesta.after(
        2100, despedir_usuario
    )


def user_abir_block(clave):
    def abrir_block():
        respuesta.insert(
            END,
            'BOOT:  Abriendo el block de notas...\n\n'
        )
        respuesta.after(
            200, abrir_block_notas
        )
        desc = respuesta.after(
            2100, activar_entry_desactivar_text
        )

    buscador.delete(
        0,
        END
    )
    respuesta.config(
        state='normal'
    )
    buscador.config(
        state='disabled',
        disabledbackground='#202123'
    )
    respuesta.insert(
        END,
        f'YO:  {clave}\n\n'
    )
    respuesta.after(
        2100, abrir_block
    )


def user_cerrar_block(clave):
    def cerrar_blcok():
        respuesta.insert(
            END,
            'BOOT:  Cerrando el block de notas...\n\n'
        )
        respuesta.after(
            200, cerrar_block_notas
        )
        desc = respuesta.after(
            2100, activar_entry_desactivar_text
        )
    buscador.delete(
        0,
        END
    )
    respuesta.config(
        state='normal'
    )
    buscador.config(
        state='disabled',
        disabledbackground='#202123'
    )
    respuesta.insert(
        END,
        f'YO:  {clave}\n\n'
    )
    respuesta.after(
        2100, cerrar_blcok
    )


def user_abrir_calc(clave):
    def abrir_calc():
        respuesta.insert(
            END,
            'BOOT:  Abriendo la calculadora...\n\n'
        )
        respuesta.after(
            200, abrir_calculadora
        )
        desc = respuesta.after(
            2100, activar_entry_desactivar_text
        )
    buscador.delete(
        0,
        END
    )
    respuesta.config(
        state='normal'
    )
    buscador.config(
        state='disabled',
        disabledbackground='#202123'
    )
    respuesta.insert(
        END,
        f'YO:  {clave}\n\n'
    )
    respuesta.after(
        2100, abrir_calc
    )


def user_cerrar_calc(clave):
    def cerrar_calc():
        respuesta.insert(
            END,
            'BOOT:  Cerrando la calculadora...\n\n'
        )
        respuesta.after(
            200, cerrar_calculadora
        )
        desc = respuesta.after(
            2100, activar_entry_desactivar_text
        )
    buscador.delete(
        0,
        END
    )
    respuesta.config(
        state='normal'
    )
    buscador.config(
        state='disabled',
        disabledbackground='#202123'
    )
    respuesta.insert(
        END,
        f'YO:  {clave}\n\n'
    )
    respuesta.after(
        2100, cerrar_calc
    )


def user_abrir_navegador(clave):
    def abrir_nv():
        respuesta.insert(
            END,
            'BOOT:  Abriendo el navegador...\n\n'
        )
        respuesta.after(
            200, abrir_navegador
        )
        desc = respuesta.after(
            2100, activar_entry_desactivar_text
        )
    buscador.delete(
        0,
        END
    )
    respuesta.config(
        state='normal'
    )
    buscador.config(
        state='disabled',
        disabledbackground='#202123'
    )
    respuesta.insert(
        END,
        f'YO:  {clave}\n\n'
    )
    respuesta.after(
        2100, abrir_nv
    )


def user_cerrar_navegador(clave):
    def cerrar_nv():
        respuesta.insert(
            END,
            'BOOT:  Cerrando el navegador...\n\n'
        )
        respuesta.after(
            200, cerrar_navegador
        )
        desc = respuesta.after(
            2100, activar_entry_desactivar_text
        )
    buscador.delete(
        0,
        END
    )
    respuesta.config(
        state='normal'
    )
    buscador.config(
        state='disabled',
        disabledbackground='#202123'
    )
    respuesta.insert(
        END,
        f'YO:  {clave}\n\n'
    )
    respuesta.after(
        2100, cerrar_nv
    )


def user_abrir_yt(clave):
    def abrir_youtube():
        respuesta.insert(
            END,
            'BOOT:  Abriendo YouTube en el navegador...\n\n'
        )
        respuesta.after(
            200, abrir_yt
        )
        desc = respuesta.after(
            2100, activar_entry_desactivar_text
        )
    buscador.delete(
        0,
        END
    )
    respuesta.config(
        state='normal'
    )
    buscador.config(
        state='disabled',
        disabledbackground='#202123'
    )
    respuesta.insert(
        END,
        f'YO:  {clave}\n\n'
    )
    respuesta.after(
        2100, abrir_youtube
    )


def user_abrir_music(clave):
    def abrir_music():
        respuesta.insert(
            END,
            'BOOT:  Abriendo la aplicación de música...\n\n'
        )
        respuesta.after(
            200, abrir_musica
        )
        desc = respuesta.after(
            2100, activar_entry_desactivar_text
        )
    buscador.delete(
        0,
        END
    )
    respuesta.config(
        state='normal'
    )
    buscador.config(
        state='disabled',
        disabledbackground='#202123'
    )
    respuesta.insert(
        END,
        f'YO:  {clave}\n\n'
    )
    respuesta.after(
        2100, abrir_music
    )


def user_cerrar_music(clave):
    def cerrar_music():
        respuesta.insert(
            END,
            'BOOT:  Cerrando la aplicación de música...\n\n'
        )
        respuesta.after(
            200, cerrar_musica
        )
        desc = respuesta.after(
            2100, activar_entry_desactivar_text
        )
    buscador.delete(
        0,
        END
    )
    respuesta.config(
        state='normal'
    )
    buscador.config(
        state='disabled',
        disabledbackground='#202123'
    )
    respuesta.insert(
        END,
        f'YO:  {clave}\n\n'
    )
    respuesta.after(
        2100, cerrar_music
    )


def user_abrir_itunes(clave):
    def abre_itun():
        respuesta.insert(
            END,
            'BOOT:  Abriendo iTunes...\n\n'
        )
        respuesta.after(
            200, abrir_itunes
        )
        desc = respuesta.after(
            2100, activar_entry_desactivar_text
        )
    buscador.delete(
        0,
        END
    )
    respuesta.config(
        state='normal'
    )
    buscador.config(
        state='disabled',
        disabledbackground='#202123'
    )
    respuesta.insert(
        END,
        f'YO:  {clave}\n\n'
    )
    respuesta.after(
        2100, abre_itun
    )


def user_cerrar_itunes(clave):
    def cerrar_itun():
        respuesta.insert(
            END,
            'BOOT:  Cerrando iTunes...\n\n'
        )
        respuesta.after(
            200, cerrar_itunes
        )
        desc = respuesta.after(
            2100, activar_entry_desactivar_text
        )
    buscador.delete(
        0,
        END
    )
    respuesta.config(
        state='normal'
    )
    buscador.config(
        state='disabled',
        disabledbackground='#202123'
    )
    respuesta.insert(
        END,
        f'YO:  {clave}\n\n'
    )
    respuesta.after(
        2100, cerrar_itun
    )


def user_abrir_spoty(clave):
    def abre_spoty():
        respuesta.insert(
            END,
            'BOOT:  Abriendo Spotify...\n\n'
        )
        respuesta.after(
            200, abrir_spotify
        )
        desc = respuesta.after(
            2100, activar_entry_desactivar_text
        )
    buscador.delete(
        0,
        END
    )
    respuesta.config(
        state='normal'
    )
    buscador.config(
        state='disabled',
        disabledbackground='#202123'
    )
    respuesta.insert(
        END,
        f'YO:  {clave}\n\n'
    )
    respuesta.after(
        2100, abre_spoty
    )


def user_cerrar_spoty(clave):
    def cerrar_spoty():
        respuesta.insert(
            END,
            'BOOT:  Cerrando Spotify...\n\n'
        )
        respuesta.after(
            200, cerrar_spotify
        )
        desc = respuesta.after(
            2100, activar_entry_desactivar_text
        )
    buscador.delete(
        0,
        END
    )
    respuesta.config(
        state='normal'
    )
    buscador.config(
        state='disabled',
        disabledbackground='#202123'
    )
    respuesta.insert(
        END,
        f'YO:  {clave}\n\n'
    )
    respuesta.after(
        2100, cerrar_spoty
    )


def user_abrir_explorador_arch(clave):
    def abrir_arch():
        respuesta.insert(
            END,
            'BOOT:  Abriendo el Explorador de Archivos...\n\n'
        )
        respuesta.after(
            200, abrir_explorador_archivos
        )
        desc = respuesta.after(
            2100, activar_entry_desactivar_text
        )
    buscador.delete(
        0,
        END
    )
    respuesta.config(
        state='normal'
    )
    buscador.config(
        state='disabled',
        disabledbackground='#202123'
    )
    respuesta.insert(
        END,
        f'YO:  {clave}\n\n'
    )
    respuesta.after(
        2100, abrir_arch
    )


def user_abrir_riot_games(clave):
    def abrir_riot_gm():
        respuesta.insert(
            END,
            'BOOT:  Abriendo Riot Games...\n\n'
        )
        respuesta.after(
            200, abrir_riot_games
        )
        desc = respuesta.after(
            2100, activar_entry_desactivar_text
        )
    buscador.delete(
        0,
        END
    )
    respuesta.config(
        state='normal'
    )
    buscador.config(
        state='disabled',
        disabledbackground='#202123'
    )
    respuesta.insert(
        END,
        f'YO:  {clave}\n\n'
    )
    respuesta.after(
        2100, abrir_riot_gm
    )


def user_cerrar_riot_games(clave):
    def cerrar_riot_gm():
        respuesta.insert(
            END,
            'BOOT:  Cerrando Riot Games...\n\n'
        )
        respuesta.after(
            200, cerrar_riot_games
        )
        desc = respuesta.after(
            2100, activar_entry_desactivar_text
        )
    buscador.delete(
        0,
        END
    )
    respuesta.config(
        state='normal'
    )
    buscador.config(
        state='disabled',
        disabledbackground='#202123'
    )
    respuesta.insert(
        END,
        f'YO:  {clave}\n\n'
    )
    respuesta.after(
        2100, cerrar_riot_gm
    )


def user_abrir_vsc(clave):
    def abrir_vsc():
        respuesta.insert(
            END,
            'BOOT:  Abriendo Visual Studio Code...\n\n'
        )
        respuesta.after(
            200, abrir_visual_studio_code
        )
        desc = respuesta.after(
            2100, activar_entry_desactivar_text
        )
    buscador.delete(
        0,
        END
    )
    respuesta.config(
        state='normal'
    )
    buscador.config(
        state='disabled',
        disabledbackground='#202123'
    )
    respuesta.insert(
        END,
        f'YO:  {clave}\n\n'
    )
    respuesta.after(
        2100, abrir_vsc
    )


def user_cerrar_vsc(clave):
    def cerrar_vsc():
        respuesta.insert(
            END,
            'BOOT:  Cerrando Visual Studio Code...\n\n'
        )
        respuesta.after(
            200, cerrar_visual_studio_code
        )
        desc = respuesta.after(
            2100, activar_entry_desactivar_text
        )
    buscador.delete(
        0,
        END
    )
    respuesta.config(
        state='normal'
    )
    buscador.config(
        state='disabled',
        disabledbackground='#202123'
    )
    respuesta.insert(
        END,
        f'YO:  {clave}\n\n'
    )
    respuesta.after(
        2100, cerrar_vsc
    )


def user_abrir_taskmgr(clave):
    def abrir_task():
        respuesta.insert(
            END,
            'BOOT:  Abriendo el administrador de tareas...\n\n'
        )
        respuesta.after(
            200, abrir_taskmgr
        )
        desc = respuesta.after(
            2100, activar_entry_desactivar_text
        )
    buscador.delete(
        0,
        END
    )
    respuesta.config(
        state='normal'
    )
    buscador.config(
        state='disabled',
        disabledbackground='#202123'
    )
    respuesta.insert(
        END,
        f'YO:  {clave}\n\n'
    )
    respuesta.after(
        2100, abrir_task
    )


def user_cerrar_taskmgr(clave):
    def cerrar_task():
        respuesta.insert(
            END,
            'BOOT:  Cerrando el administrador de tareas...\n\n'
        )
        respuesta.after(
            200, cerrar_taskmgr
        )
        desc = respuesta.after(
            2100, activar_entry_desactivar_text
        )
    buscador.delete(
        0,
        END
    )
    respuesta.config(
        state='normal'
    )
    buscador.config(
        state='disabled',
        disabledbackground='#202123'
    )
    respuesta.insert(
        END,
        f'YO:  {clave}\n\n'
    )
    respuesta.after(
        2100, cerrar_task
    )

# Función -> Búsqueda


def busquedas(clave):
    """Muestra la información"""
    if clave in saludar:
        user_saludar(clave)
    elif clave in salir:
        user_salir(clave)
    elif clave in abre_block_notas:
        user_abir_block(clave)
    elif clave in cierra_block_notas:
        user_cerrar_block(clave)
    elif clave in abre_calculadora:
        user_abrir_calc(clave)
    elif clave in cierra_claculadora:
        user_cerrar_calc(clave)
    elif clave in abre_navevagor:
        user_abrir_navegador(clave)
    elif clave in cierra_navegador:
        user_cerrar_navegador(clave)
    elif clave in abre_yt:
        user_abrir_yt(clave)
    elif clave in abre_musica:
        user_abrir_music(clave)
    elif clave in cierra_musica:
        user_cerrar_music(clave)
    elif clave in abre_app_musica_itunes:
        user_abrir_itunes(clave)
    elif clave in cierra_app_musica_itunes:
        user_cerrar_itunes(clave)
    elif clave in abre_app_musica_spotify:
        user_abrir_spoty(clave)
    elif clave in cierra_app_musica_spotify:
        user_cerrar_spoty(clave)
    elif clave in abre_explorador_archivos:
        user_abrir_explorador_arch(clave)
    elif clave in abre_riot_gamaes:
        user_abrir_riot_games(clave)
    elif clave in cierra_riot_games:
        user_cerrar_riot_games(clave)
    elif clave in abre_visual_studio_code:
        user_abrir_vsc(clave)
    elif clave in cierra_visual_studio_code:
        user_cerrar_vsc(clave)
    elif clave in abre_administrador_tareas:
        user_abrir_taskmgr(clave)
    elif clave in cierra_administrador_tareas:
        user_cerrar_taskmgr(clave)
    else:
        buscador.delete(
            0,
            END
        )
        messagebox.showerror(
            'Error', f'La palabra {clave} no existe, espera actualizaciones'
        )


def buscador_searches():
    """Busca la información con la palabra clave"""
    clave = Searches.get()
    busquedas(clave)


# App #

# Visual
ventana.attributes(
    '-fullscreen', True
)
ventana.title(
    'CHAT BOOT'
)
ventana.iconbitmap(
    r'images\icon-app.ico'
)
ventana.config(
    background='#202123'
)

# Visual -> Panel izquierdo -> Panel derecho

panel_izq = Label(
    ventana,
    background='#232a38'
)
panel_izq.place(
    width=400,
    height=1080,
    x=0,
    y=0
)

panel_der = Label(
    ventana,
    background='#232a38'
)

panel_der.place(
    width=400,
    height=1080,
    x=1520,
    y=0
)

# Bienvenida

bienvenida = Label(
    ventana,
    text='BIENVENIDO!!',
    font=(
        'Arial Black', 45
    ),
    background='#202123',
    foreground='white'
)

bienvenida.place(
    x=725,
    y=50
)

# Buscador

buscador = Entry(
    ventana,
    textvariable=Searches,
    justify='center',
    background='#202123',
    foreground='white',
    font=(
        'Arial', 20
    )
)

buscador.place(
    width=1000,
    height=50,
    x=460,
    y=950
)

buscador.delete(
    0,
    'end'
)

# Chat -> Scrollbar

respuesta = Text(
    ventana,
    background='#202123',
    foreground='white',
    state='normal',
    font=(
        'Arial', 15
    ),
    border=0
)

respuesta.place(
    width=980,
    height=799,
    x=460,
    y=150
)

respuesta.insert(
    'end',
    '\n'
)

barra_de_desplazamiento = Scrollbar(
    ventana,
    command=respuesta.yview,
    cursor='hand2'
)


barra_de_desplazamiento.place(
    width=20,
    height=799,
    x=1440,
    y=150
)


respuesta.config(
    yscrollcommand=barra_de_desplazamiento.set,
    state='disabled'
)


# Botón borrar contenido

boton_clear_img = PhotoImage(
    file=r'images\clear.png'
)

boton_clear = Button(
    ventana,
    image=boton_clear_img,
    background='#232a38',
    activebackground='#232a38',
    command=lambda: [
        {
            borrar_chat()
        }
    ],
    border=0,
    cursor='hand2'
)

boton_clear.place(
    x=1700,
    y=400
)

# Funciones del teclado


ventana.bind(
    '<Return>', lambda event: buscador_searches()
)

ventana.mainloop()
