from tkinter import *
window = Tk()
window.geometry("600x500")
def convert():
    Celsius_value = float(entry.get())
    Fahrenheit_value = Celsius_value * (9/5) + 32
    print(Fahrenheit_value)
    label3.config(text = "Temperature in Fahrenheit :" + str(Fahrenheit_value))
label = Label(window, text = "Celsius -> Fahrenheit", font = ("Calibra", 20 ))
label.place(x=155,y=50)
label2 = Label(window, text = "Enter Temperature in Celsius:", font = ("Calibra", 10))
label2.place(x=75,y=120)
entry = Entry(window)
entry.place(x=285,y=120)
label3 = Label(window, text = "Temperature in Fahrenheit : ", font = ("Calibra",  13))
label3.place(x=90,y=180)
button = Button(window, text = "CONVERT", font = ("Calibra", 10), command = convert)
button.place(x=275, y=300)




window.mainloop()