import subprocess
import os

# // Exit Aplicacion \\ #


def system_exit_aplicacion():
    print(
        exit(

        )
    )


# // Open Block De Notas \\ #


def system_open_notepad():
    subprocess.Popen(
        [
            'notepad.exe'
        ],
        start_new_session=True
    )

# // Close Block de Notas \\ #


def system_close_notepad():
    subprocess.Popen(
        [
            'taskkill',
            '/f',
            '/im',
            'notepad.exe'
        ]
    )

# // Open Calculadora \\ #


def system_open_calculadora():
    os.system(
        'start calc'
    )


# // Close Calculadora \\ #


def system_close_calculadora():
    subprocess.Popen(
        [
            'taskkill',
            '/f',
            '/im',
            'CalculatorApp.exe'
        ]
    )


# // Close Navegador \\ #


def system_close_navegador():
    subprocess.call(
        [
            "taskkill",
            "/f",
            "/im",
            "msedge.exe"
        ]
    )


# // Open iTunes \\ #


def system_open_itunes():
    subprocess.Popen(
        [
            'iTunes.exe'
        ],
        start_new_session=True
    )


# // Close iTunes \\ #


def system_close_itunes():
    subprocess.Popen(
        [
            'taskkill',
            '/f',
            '/im',
            'iTunes.exe'
        ]
    )


# // Open Explorador de Archivos \\ #


def system_open_explorador_archivos():
    subprocess.Popen(
        [
            'explorer.exe'
        ],
        start_new_session=True
    )


# // Open Riot Games \\ #


def system_open_riot_games():
    subprocess.Popen(
        [
            'C:/Riot Games/Riot Client/RiotClientServices.exe'
        ]
    )


# // Close Riot Games \\ #


def system_close_riot_games():
    subprocess.Popen(
        [
            'taskkill',
            '/f',
            '/im',
            'RiotClientServices.exe'
        ]
    )


# // Open VSC \\ #


def system_open_vsc():
    os.system(
        'Code'
    )


# // Close VSC \\ #


def system_close_vsc():
    subprocess.Popen(
        [
            'taskkill',
            '/f',
            '/im',
            'Code.exe'
        ]
    )


# // Open Administrador de Tareas \\ #


def system_open_taskmgr():
    subprocess.Popen(
        [
            'Taskmgr.exe'
        ]
    )


# // Close Administrador de Tareas \\ #


def system_close_taskmgr():
    subprocess.Popen(
        [
            'taskkill',
            '/f',
            '/im',
            'Taskmgr.exe'
        ]
    )
