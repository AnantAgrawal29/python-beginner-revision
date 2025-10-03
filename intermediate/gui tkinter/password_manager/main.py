from tkinter import *
from tkinter import messagebox
import random
import json

# import pyperclip

# ---------------------------- SEARCH WEBSITE ------------------------------- #


def search_data():
    website_name = website_input.get()
    if not website_name:
        messagebox.showwarning(title="Error", message="No website name provided")
    else:
        try:
            with open(file="data.json", mode="r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            messagebox.showerror(
                title="Data Not found",
                message="No Data File Found",
            )
        else:
            try:
                email = data[website_name]["email"]
                password = data[website_name]["password"]
            except KeyError:
                messagebox.showerror(
                    title="No Entry Found",
                    message=f"No data related to {website_name} found",
                )
            else:
                messagebox.showinfo(
                    title=website_name,
                    message=f"These are the details: \nEmail: {email}\nPassword: {password}",
                )


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pass():
    letters = [chr(num) for num in range(97, 123)]
    letters.extend([chr(num) for num in range(65, 91)])
    numbers = [str(num) for num in range(10)]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
    # pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def addEntry():
    website_name = website_input.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {f"{website_name}": {"email": email, "password": password}}
    if not website_name:
        messagebox.showwarning(title="Error", message="No website name provided")
    elif not password:
        messagebox.showwarning(title="Error", message="No password provided")
    else:
        is_ok = messagebox.askokcancel(
            title=website_name,
            message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?",
        )
        if is_ok:
            try:
                with open(file="data.json", mode="r") as file:
                    data = json.load(file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                with open(file="data.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open(file="data.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                pass_entry.delete(0, END)
                website_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=0)

# Labels
website = Label(text="Website:")
website.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

# Entries
website_input = Entry(width=35)
website_input.grid(column=1, row=1, sticky="EW")

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "anant@gmail.com")

pass_entry = Entry(width=26)
pass_entry.grid(column=1, row=3, padx=(0, 2), sticky="EW")

# Buttons

search = Button(text="Search", highlightthickness=0, command=search_data)
search.grid(column=2, row=1, sticky="EW")

generate = Button(
    text="Generate Password ", highlightthickness=0, command=generate_pass
)
generate.grid(column=2, row=3)

add = Button(text="Add", width=32, highlightthickness=0, command=addEntry)
add.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
