from tkinter import *

def button_clicked():
    print("I got clicked.")
    new_text = input.get()
    my_label["text"] = new_text

window = Tk()
window.title("My Second GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


#Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x= 0, y= 0)
my_label.grid(column= 0, row= 0)

#Edit the label text:
my_label["text"] = "New Text"
my_label.config(text="New Text")

#Button

button = Button(text="Click Me", command=button_clicked)
button2 = Button(text="Click Me Too", command=button_clicked)
# button.pack()
button.grid(column= 2, row= 2)
button2.grid(column= 3, row= 1)


#Input
input = Entry(width=10)
# input.pack()
input.grid(column= 4, row= 3)




window.mainloop()