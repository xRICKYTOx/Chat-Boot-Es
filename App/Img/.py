from tkinter import *


windows = Tk()

windows.title(
    'UPDATE'
)
windows.iconbitmap(
    r'C:\CHAT-BOOT\App\Img\update.ico'
)
windows.geometry(
    '500x200+710+440'
)
windows.overrideredirect(
    True
)
windows.resizable(
    0, 0
)
windows.config(
    background='white'
)
panel = Label(
    windows,
    background='#202123'
)
panel.place(
    x=10,
    y=10,
    width=480,
    height=180
)
ver = Label(
    windows,
    background='#202123',
    foreground='white',
    font=(
        'Arial Black', 30
    ),
    text='Update ver 1.0.0'
)

ver.place(
    x=60,
    y=30
)

button = Button(
    windows,
    text='CONTINUAR',
    font=(
        'Arial', 18
    ),
    background='#202123',
    foreground='white',
    activebackground='white',
    activeforeground='grey',
    cursor='hand2',
    border=2,
    command=lambda: [
        {

        }
    ]
)

button.place(
    x=170,
    y=115
)

windows.mainloop()
