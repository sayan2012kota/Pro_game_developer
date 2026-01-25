from tkinter import *
from tkinter import messagebox
from random import randint
window = Tk()
window.geometry("600x400")
number = randint(1, 20)
def greet_player():
    name = entry.get()
    messagebox.showinfo("Guess the number", "Hello " + name +", I am thinking of a number between 1 and 20. Guess what the number is.")
def give_hint():
    submission = int(entry2.get())
    if submission > number:
        messagebox.showinfo("Hint", "Your number is too high")
    if submission < number:
        messagebox.showinfo("Hint", "Your number is too low")
    if submission == number:
        messagebox.showinfo("You Win!", "Congrats, you got it right!")
        window.destroy()
    


label = Label(window, text = "Welcome to guessing game", font = ("Calibra", 14))
label.place(x=100, y=50)
label2 = Label(window, text = "Enter your name", font = ("Calibra", 10))
label2.place(x=25, y=80)
entry = Entry(window)
entry.place(x=25, y=100)
button = Button(window, text = "OK", font = ("Calibra", 10), command = greet_player)
button.place(x=250, y=100)
label3 = Label(window, text = "Guess the number in this text box:", font = ("Calibra, 10"))
label3.place(x=25, y=300)
entry2 = Entry(window)
entry2.place(x=25, y=325)
button2 = Button(window, text = "Submit", font = ("Calibra", 10), command = give_hint)
button2.place(x=250, y=325)





window.mainloop()