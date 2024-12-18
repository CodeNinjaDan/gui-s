import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(numbers) for _ in range(randint(2, 4))]
    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) <= 10:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            # If file doesn't exist, start with an empty dictionary
            # data = {}
            with open("data.json","w")as data_file:
                json.dump(new_data,data_file, indent=4)

        # except json.JSONDecodeError:
        #     # If file is empty or invalid JSON, start with an empty dictionary
        #     data = {}

        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH --------------------------------- #

def find_password():
    search_key = website_entry.get()

    try:
        with open("data.json", "r") as file_data:
            data = json.load(file_data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file exists!")

    else:
        if search_key in data:
            email = data[search_key]["email"]
            password = data[search_key]["password"]
            messagebox.showinfo(title=search_key, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {search_key} exists!")


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


website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_entry = Entry(width=21)
email_entry.grid(column=1, row=2)
email_entry.insert(END, "@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)


generate_button = Button(text="Generate Password", command=generate_password)
save_button = Button(text="Add", width=36, command=save)
generate_button.grid(column=2, row=3)
save_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1)


window.mainloop()
