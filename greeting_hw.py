from tkinter import *
from tkinter import messagebox
def button_command():
    messagebox.showinfo("Welcome", "Welcome to python tkinter!")
window = Tk()
window.geometry("200x200")
button = Button(window, text = "Click for a Message", command = button_command)
button.place(x=50, y=50)



window.mainloop()