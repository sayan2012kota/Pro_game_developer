from tkinter import *
window = Tk()
window.geometry("250x600")
label = Label(window, text = "Shopping List")
label.pack(side=TOP)
scrollbar = Scrollbar(window)
scrollbar.pack(side = RIGHT, fill=Y)
listbox = Listbox(window, height = 20, width=20, yscrollcommand=scrollbar.set, bg= "brown", fg="yellow")
scrollbar.config(command=listbox.yview)
listbox.place(x=50, y=50)
for i in range(20):
    listbox.insert(END, "Grocery Item", i)
button = Button(window, text = "CHECKOUT", font = ("Calibra", 15))
button.place(x=50, y=500)




window.mainloop()