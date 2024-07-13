import tkinter
from tkinter import *
from tkinter import messagebox
from controllers import loadDock

# настройка интерфейса
root = Tk()

root['bg'] = '#fafafa'
root.title('Название программы')
root.wm_attributes('-alpha', 1)
root.geometry('600x500')

root.resizable(width=True, height=True)

canvas = Canvas(root, height=600, width=500)
canvas.pack()

# frame = Frame(root, bg='red')
# frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

# tittle = Label(frame, text='Текст подсказка', bg='gray', font=40)
# tittle.pack()

btnLoad = Button(canvas,
                 text='Нажмите, чтобы загрузить документ',
                 bg='white',
                 justify=tkinter.CENTER,
                 width=600,
                 height=500,
                 command=loadDock.dockLoad)
btnLoad.pack()

if __name__ == '__main__':
    root.mainloop()