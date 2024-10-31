from tkinter import *

window = Tk()
window.minsize(width=500, height=250)
window.title("Miles to Km converter")
window.config(padx=100, pady= 100)

def calculate():
    miles = int(entry.get())
    km = miles * 1.609344
    result_label.config(text=f"{km:.2f}")


entry = Entry(width=5)
entry.insert(END, string= "0")
entry.focus()
entry.grid(column=1, row=0)


label1 =Label(text="Miles")
label2 =Label(text="is equal to")
label3 =Label(text="Km")
label1.grid(column= 2, row= 0)
label2.grid(column= 0, row= 1)
label3.grid(column= 2, row= 1)



result_label = Label(text="0")
result_label.grid(column=1, row=1)


button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)





window.mainloop()