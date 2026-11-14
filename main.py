from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle


# Generate Password
def generate_password():
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("0123456789")
    symbols = list("!@#$%^&*()+")

    password_letters = [
        choice(letters) for _ in range(randint(8, 10))
    ]

    password_symbols = [
        choice(symbols) for _ in range(randint(2, 4))
    ]

    password_numbers = [
        choice(numbers) for _ in range(randint(2, 4))
    ]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)


# Save Password
def save():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops",
            message="Please don't leave Website or Password empty."
        )

    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"Website: {website}\n"
                    f"Email: {email}\n"
                    f"Password: {password}\n\n"
                    "Is it okay to save?"
        )

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(
                    f"{website} | {email} | {password}\n"
                )

            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

            messagebox.showinfo(
                title="Success",
                message="Password saved successfully!"
            )


# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=40, bg="#EAF2F8")
window.resizable(False, False)

# Colors
BACKGROUND = "#EAF2F8"
DARK_BLUE = "#172554"
BLUE = "#2563EB"
GREEN = "#16A34A"
WHITE = "#FFFFFF"
TEXT_COLOR = "#1E293B"

# Heading
title_label = Label(
    text="🔐 PASSWORD MANAGER",
    font=("Arial", 20, "bold"),
    bg=BACKGROUND,
    fg=DARK_BLUE
)
title_label.grid(row=0, column=0, columnspan=3, pady=(0, 25))

# Labels
website_label = Label(
    text="Website:",
    font=("Arial", 11, "bold"),
    bg=BACKGROUND,
    fg=TEXT_COLOR
)
website_label.grid(row=1, column=0, sticky="w", pady=8)

email_label = Label(
    text="Email / Username:",
    font=("Arial", 11, "bold"),
    bg=BACKGROUND,
    fg=TEXT_COLOR
)
email_label.grid(row=2, column=0, sticky="w", pady=8)

password_label = Label(
    text="Password:",
    font=("Arial", 11, "bold"),
    bg=BACKGROUND,
    fg=TEXT_COLOR
)
password_label.grid(row=3, column=0, sticky="w", pady=8)

# Entry
entry_style = {
    "width": 35,
    "font": ("Arial", 11),
    "bg": WHITE,
    "fg": TEXT_COLOR,
    "relief": FLAT,
    "bd": 5
}

website_entry = Entry(**entry_style)
website_entry.grid(row=1, column=1, columnspan=2, pady=8, ipady=5)
website_entry.focus()

email_entry = Entry(**entry_style)
email_entry.grid(row=2, column=1, columnspan=2, pady=8, ipady=5)
email_entry.insert(0, "your_email@example.com")

password_entry = Entry(
    width=22,
    font=("Arial", 11),
    bg=WHITE,
    fg=TEXT_COLOR,
    relief=FLAT,
    bd=5
)
password_entry.grid(row=3, column=1, pady=8, ipady=5)

# Button
generate_password_button = Button(
    text="Generate Password",
    command=generate_password,
    bg=BLUE,
    fg=WHITE,
    activebackground="#1D4ED8",
    activeforeground=WHITE,
    font=("Arial", 9, "bold"),
    relief=FLAT,
    cursor="hand2",
    padx=8,
    pady=7
)
generate_password_button.grid(row=3, column=2, padx=(5, 0))

add_button = Button(
    text="SAVE PASSWORD",
    command=save,
    width=35,
    bg=GREEN,
    fg=WHITE,
    activebackground="#15803D",
    activeforeground=WHITE,
    font=("Arial", 11, "bold"),
    relief=FLAT,
    cursor="hand2",
    pady=9
)
add_button.grid(row=4, column=1, columnspan=2, pady=20)

# Footer
footer_label = Label(
    text="Keep your passwords organized!",
    font=("Arial", 9, "italic"),
    bg=BACKGROUND,
    fg="#64748B"
)
footer_label.grid(row=5, column=0, columnspan=3, pady=(5, 0))

# Main Loop
window.mainloop()
