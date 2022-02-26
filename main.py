from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    data_website = website_entry.get()
    data_email = email_entry.get()
    data_password = password_entry.get()
    new_data = f"{data_website} | {data_email} | {data_password} \n"
    if len(data_website)==0 or len(data_password)==0 or len(data_email)==0:
        messagebox.showerror(title="Empty spaces", message="Don'n leave empty spaces")
    else:
        save_or_not = messagebox.askokcancel(title=data_website, message=f"Look if your datas are right\n"
                                                                         f"Email: {data_email}\n"
                                                                         f"Password: {data_password}\n"
                                                                         f"Save or not?")
        if save_or_not:
            with open("data.txt","a") as data_file:
                data_file.write(new_data)
                data_file.close()
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

# creating the window
window = Tk()
window.title("Password Generator")
window.config(pady=50, padx=50, bg="white")

# creating the canvas image
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# creating labels

website_label = Label(text=" WebSite: ", bg="white", fg="black", font=("Arial", 10, "bold"))
website_label.grid(row=1, column=0)

email_label = Label(text=" Email / Username: ", bg="white", fg="black", font=("Arial", 10, "bold"))
email_label.grid(row=2, column=0)

password_label = Label(text=" Password: ", bg="white", fg="black", font=("Arial", 10, "bold"))
password_label.grid(row=3, column=0)

# creating the entrys

website_entry = Entry(width=53)
website_entry.grid(row=1, column=1 , columnspan=2)
website_entry.focus()

email_entry = Entry(width=53)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"mariomgsb@gmail.com")

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

# creating buttons

generate_button = Button(text="Generate Password", bg="white", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", bg="white", width=45,command=add)
add_button.grid(row=4, column=1, columnspan=2)



# looping the screen to not close
window.mainloop()
