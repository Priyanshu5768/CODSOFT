import string
import random
from tkinter import *
from tkinter import messagebox
import sqlite3

def setup_database():
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users(Username TEXT NOT NULL, GeneratedPassword TEXT NOT NULL);")
        db.commit()

class PasswordGeneratorApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Password Generator")
        self.window.geometry("660x500")
        self.window.config(bg="#FF8000")
        self.window.resizable(False, False)
        self.username = StringVar()
        self.password_length = IntVar()
        self.generated_password = StringVar()
        self.create_widgets()
    
    def create_widgets(self):
        Label(self.window, text=":PASSWORD GENERATOR:", bg="#FF8000", fg="darkblue", font="arial 20 bold underline").grid(row=0, column=1)
        Label(self.window, text="Enter User Name:", bg="#FF8000", fg="darkblue", font="times 15 bold").grid(row=2, column=0)
        Entry(self.window, textvariable=self.username, font="times 15", bd=6, relief="ridge").grid(row=2, column=1)
        Label(self.window, text="Enter Password Length:", bg="#FF8000", fg="darkblue", font="times 15 bold").grid(row=3, column=0)
        Entry(self.window, textvariable=self.password_length, font="times 15", bd=6, relief="ridge").grid(row=3, column=1)
        Label(self.window, text="Generated Password:", bg="#FF8000", fg="darkblue", font="times 15 bold").grid(row=4, column=0)
        Entry(self.window, textvariable=self.generated_password, font="times 15", bd=6, relief="ridge", fg="#DC143C").grid(row=4, column=1)
        Button(self.window, text="GENERATE PASSWORD", command=self.generate_password, bg="#BCEE68", fg="#68228B", font="Verdana 15 bold", bd=3, relief="solid").grid(row=5, column=1)
        Button(self.window, text="ACCEPT", command=self.accept_fields, bg="#FFFAF0", fg="#458B00", font="Helvetica 15 bold italic", bd=3, relief="solid").grid(row=6, column=1)
        Button(self.window, text="RESET", command=self.reset_fields, bg="#FFFAF0", fg="#458B00", font="Helvetica 15 bold italic", bd=3, relief="solid").grid(row=7, column=1)

    def generate_password(self):
        uppercase = string.ascii_uppercase
        lowercase = string.ascii_lowercase
        symbols = "@#%&()\"?!"
        digits = string.digits
        username = self.username.get()
        length = self.password_length.get()
        if not username:
            messagebox.showerror("Error", "Please enter a username")
            return
        if not username.isalpha():
            messagebox.showerror("Error", "Username must contain only letters")
            self.username.set("")
            return
        if length < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters")
            return
        password = (
            random.sample(uppercase, 1) +
            random.sample(lowercase, 1) +
            random.sample(symbols, 1) +
            random.sample(digits, 1) +
            random.sample(uppercase + lowercase + symbols + digits, length - 4)
        )
        random.shuffle(password)
        self.generated_password.set("".join(password))

    def accept_fields(self):
        username = self.username.get()
        password = self.generated_password.get()
        with sqlite3.connect("users.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM users WHERE Username = ?", (username,))
            if cursor.fetchall():
                messagebox.showerror("Error", "Username already exists!")
            else:
                cursor.execute("INSERT INTO users VALUES (?, ?)", (username, password))
                db.commit()
                messagebox.showinfo("Success", "Password saved successfully")

    def reset_fields(self):
        self.username.set("")
        self.password_length.set(0)
        self.generated_password.set("")

if __name__ == "__main__":
    setup_database()
    window = Tk()
    app = PasswordGeneratorApp(window)
    window.mainloop()