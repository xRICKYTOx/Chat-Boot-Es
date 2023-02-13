"""Abre paginas de internet"""

from webbrowser import open_new


def abrir_navegador():
    """Abre la pagina de google en el navegador"""

    open_new(
        'https://www.google.com.mx/'
    )


def abrir_yt():
    """Abre la pagina de YouTube en el navegador"""
    open_new(
        'https://www.youtube.com/'
    )
