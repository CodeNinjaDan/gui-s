from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = entry1.get()
    email = entry2.get()
    password = entry3.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        with open("data.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")
            entry1.delete(0, END)
            entry3.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file= "logo.png")
canvas.create_image(100, 100, image= img)
canvas.grid(column=1, row=0)


website_name = Label(text="Website:")
name = Label(text="Email/Username:")
words = Label(text="Password:")
website_name.grid(column=0, row=1)
name.grid(column=0, row=2)
words.grid(column=0, row=3)


entry1 = Entry(width=35)
entry1.focus()
entry1.grid(column=1, row=1, columnspan=2)

entry2 = Entry(width=35)
entry2.grid(column=1, row=2, columnspan=2)
entry2.insert(END, "@gmail.com")
entry3 = Entry(width=21)
entry3.grid(column=1, row=3)


button1 = Button(text="Generate Password")
button2 = Button(text="Add", width=36, command=save)
button1.grid(column=2, row=3)
button2.grid(column=1, row=4, columnspan=2)






window.mainloop()