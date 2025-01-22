from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, END, messagebox
# from password_generator import password
from random import choice, randint, shuffle
from string import ascii_letters, punctuation, digits
from pyperclip import copy


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_list = (
            [choice(ascii_letters) for _ in range(randint(8, 10))] +
            [choice(punctuation) for _ in range(randint(2, 4))] +
            [choice(digits) for _ in range(randint(2, 4))]
    )

    shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website and password:
        yes = messagebox.askyesno(title=website.upper(),
                                  message=f"Details entered:\nEmail: {email}\nPassword: {password}\n\nIs it okay to save?")
        if yes:
            with open("../../Files/password_data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(title="SUCCESS!", message="Password data saved successfully!")
    else:
        messagebox.showerror(title="ERROR!", message="Please don't leave any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="../../Files/my_pass.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = Entry(width=35)
email_entry.insert(0, "email@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
