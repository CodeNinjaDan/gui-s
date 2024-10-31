from tkinter import *

window = Tk()
window.title("My Second GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

#Edit the label text:
my_label["text"] = "New Text"
my_label.config(text="New Text")

#Button
def button_clicked():
    print("I got clicked.")
    new_text = input.get()
    my_label["text"] = new_text

button = Button(text="Click Me", command=button_clicked)
button.pack()

#Input
input = Entry(width=10)
input.pack()
window.mainloop()