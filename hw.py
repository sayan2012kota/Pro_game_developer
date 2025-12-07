from tkinter import *
import calendar
def month_calendar():
    second_window = Tk()
    second_window.geometry("560x620")
    year = entry.get()
    year = int(year)
    calend = calendar.calendar(year)
    label3 = Label(second_window, text = (calend))
    label3.place(x=10, y=10)
window = Tk()
window.config(background = "blue")
window.geometry("600x540")
window.resizable(False, False)
label = Label(window, text = "Calendar", background = "grey", font = ("Calibra", 100 ))
label.place(x=0, y = 0)
label2 = Label(window, text = "Enter Year", background = "light green", font = ("Calibra", 15))
label2.place(x=250, y=170)
entry = Entry(window, width = 25)
entry.place(x=210, y=200)
button = Button(window, text = "Show Calendar", background = "red", font = ("Calibra", 17), width = 15, command = month_calendar)
button.place(x=185, y=221)
button2 = Button(window, text = "Exit", background = "red", font = ("Calibra", 17), width = 5, command=window.destroy)
button2.place(x=255, y=268)

                
window.mainloop()