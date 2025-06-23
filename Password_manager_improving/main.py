import json
from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for sym in range(randint(2, 4))]
    password_list += [choice(numbers) for num in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)  # password in clipboard
    input_password.delete(0, END)  # Clear any existing text
    input_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    # f = open("data.txt", "a")
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if website == "" or email == "" or password == "":
        messagebox.showwarning(title="Oops", message="Please don't let any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save ?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
                    # pass
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file)
            else:

                data.update(new_data)
                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)

            input_website.delete(0, END)
            input_password.delete(0, END)
            input_website.focus()


def find_password():
    website = input_website.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            if website in data:
                messagebox.showinfo(title=website,
                                    message=f"Email: {data[website]['email']}\npassword: {data[website]['password']}")
            else:
                messagebox.showwarning(message="No details for the website exists")

    except:
        messagebox.showwarning(message="No data file for the website exists")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager Start")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", width=21)
password_label.grid(column=0, row=3)

# Entry
input_website = Entry(width=35)
input_website.focus()
input_website.grid(column=1, row=1, sticky="ew")
input_email = Entry(width=35)
input_email.insert(0, "hiba@gmail.com")
input_email.grid(column=1, row=2, columnspan=2, sticky="ew")
input_password = Entry(width=21)
input_password.grid(column=1, row=3, sticky="ew")
##


# Buttons
add_button = Button(text="Add", width=36, command=add_data)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew")
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="ew")
window.mainloop()
