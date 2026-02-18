from tkinter import *
from tkinter import messagebox
root = Tk()

def btn_click():
    
    print('Hello world!')
    login = loginInput.get()
    password = passField.get()
    if login != "":
        info_str = f"Данні: {str(login)}, {str(password)} " 
        messagebox.showinfo(title="Назва", message=info_str)
    else:
    # окно с ошибкой
        messagebox.showerror(title="", message="Er")
root["bg"] = '#fafafa' 
root.title('мое приложение')
root.wm_attributes('-alpha', 0.7)
root.geometry("300x250")

root.resizable(width=False, height=False)

canvas = Canvas(root,height=300,width=250)
canvas.pack()

frame = Frame(root, bg="red")
frame.place(relx=0.15, rely=0.15, relheight=0.8, relwidth=0.7)

title = Label(frame, text="чето тут я напишу", bg='gray', font=40)
title.pack()
btn = Button(frame, text='Кнопка', bg='yellow', command=btn_click)
btn.pack()

loginInput = Entry(frame, bg='white')
loginInput.pack()

passField = Entry(frame, bg='white', show="*")
passField.pack()

root.mainloop()












