
'''
import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Label 1", bg="red", fg="white")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Label 2", bg="green", fg="white")
label2.grid(row=0, column=1)

label3 = tk.Label(root, text="Label 3", bg="blue", fg="white")
label3.grid(row=1, column=0, columnspan=2, sticky=tk.W+tk.E)

root.mainloop()

--->
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter Window")
root.geometry("300x200")  # Set the window size

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=20)  # Pack the label into the window with padding

# Create a button widget
button = tk.Button(root, text="Click Me", font=("Arial", 12), command=lambda: label.config(text="Button Clicked!"))
button.pack(pady=10)  # Pack the button into the window with padding

# Start the Tkinter event loop
root.mainloop()
'''

'''import tkinter as tk
from datetime import date

class DataEntryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Data Entry Application")

        # Create labels and entry fields
        name_label = tk.Label(self, text="Name:")
        name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        age_label = tk.Label(self, text="Age:")
        age_label.grid(row=1, column=0, padx=10, pady=5)
        self.age_entry = tk.Entry(self)
        self.age_entry.grid(row=1, column=1, padx=10, pady=5)

        village_label = tk.Label(self, text="Village:")
        village_label.grid(row=2, column=0, padx=10, pady=5)
        self.village_entry = tk.Entry(self)
        self.village_entry.grid(row=2, column=1, padx=10, pady=5)

        purpose_label = tk.Label(self, text="Purpose:")
        purpose_label.grid(row=3, column=0, padx=10, pady=5)
        self.purpose_entry = tk.Entry(self)
        self.purpose_entry.grid(row=3, column=1, padx=10, pady=5)

        date_label = tk.Label(self, text="Date:")
        date_label.grid(row=4, column=0, padx=10, pady=5)
        self.date_entry = tk.Entry(self)
        self.date_entry.grid(row=4, column=1, padx=10, pady=5)

        # Create a button to submit the data
        submit_button = tk.Button(self, text="Submit", command=self.submit_data)
        submit_button.grid(row=5, column=1, padx=10, pady=10)

    def submit_data(self):
        # Get the entered data
        name = self.name_entry.get()
        age = self.age_entry.get()
        village = self.village_entry.get()
        purpose = self.purpose_entry.get()
        date = self.date_entry.get()

        # Validate the data (you can add more validation checks as needed)
        if not name or not age or not village or not purpose or not date:
            tk.messagebox.showwarning("Error", "Please fill in all fields.")
            return

        try:
            age = int(age)
        except ValueError:
            tk.messagebox.showwarning("Error", "Age must be a number.")
            return

        # Process the data (e.g., save it to a file, database, or perform other actions)
        print("Name:", name)
        print("Age:", age)
        print("Village:", village)
        print("Purpose:", purpose)
        print("Date:", date)

        # Clear the entry fields for the next entry
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.village_entry.delete(0, tk.END)
        self.purpose_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

if __name__ == "__main__":
    app = DataEntryApp()
    app.mainloop()
'''

########## A
# 

import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import simpledialog
import sqlite3
from datetime import datetime

class HospitalDataEntryApp:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Hospital Data Entry Application")
        
        # Connect to the SQLite database
        self.conn = sqlite3.connect("hospital.db")
        self.cursor = self.conn.cursor()
        
        # Create table if it doesn't exist
        self.create_table()

        # Setup the user interface
        self.setup_ui()

    def create_table(self):
        """Creates the patients table if it does not exist."""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            contact TEXT NOT NULL,
            disease TEXT NOT NULL,
            date TEXT NOT NULL
        )
        """)
        self.conn.commit()

    def setup_ui(self):
        """Sets up the user interface for the application."""
        # Patient details frame
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack()

        # Patient Name
        tk.Label(frame, text="Patient Name:").grid(row=0, column=0, pady=5)
        self.entry_name = tk.Entry(frame)
        self.entry_name.grid(row=0, column=1, pady=5)

        # Age
        tk.Label(frame, text="Age:").grid(row=1, column=0, pady=5)
        self.entry_age = tk.Entry(frame)
        self.entry_age.grid(row=1, column=1, pady=5)

        # Gender
        tk.Label(frame, text="Gender:").grid(row=2, column=0, pady=5)
        self.gender_var = tk.StringVar(value="Male")
        tk.Radiobutton(frame, text="Male", variable=self.gender_var, value="Male").grid(row=2, column=1, sticky=tk.W)
        tk.Radiobutton(frame, text="Female", variable=self.gender_var, value="Female").grid(row=2, column=2, sticky=tk.W)

        # Contact No
        tk.Label(frame, text="Contact No:").grid(row=3, column=0, pady=5)
        self.entry_contact = tk.Entry(frame)
        self.entry_contact.grid(row=3, column=1, pady=5)

        # Disease
        tk.Label(frame, text="Disease:").grid(row=4, column=0, pady=5)
        self.entry_disease = tk.Entry(frame)
        self.entry_disease.grid(row=4, column=1, pady=5)

        # Date (Manual Entry)
        tk.Label(frame, text="Date (YYYY-MM-DD):").grid(row=5, column=0, pady=5)
        self.entry_date = tk.Entry(frame)
        self.entry_date.grid(row=5, column=1, pady=5)

        # Save and Clear buttons
        save_button = tk.Button(frame, text="Save", command=self.save_data)
        save_button.grid(row=6, column=0, pady=20)

        clear_button = tk.Button(frame, text="Clear", command=self.clear_data)
        clear_button.grid(row=6, column=1, pady=20)

        # Retrieve Button
        retrieve_button = tk.Button(frame, text="Retrieve Data", command=self.retrieve_data)
        retrieve_button.grid(row=7, column=0, pady=10)

        # TreeView for displaying retrieved data
        columns = ("id", "name", "age", "gender", "contact", "disease", "date")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col.capitalize())
        self.tree.pack(pady=20)

    def save_data(self):
        """Saves the patient's data into the database."""
        # Get data from entry fields
        name = self.entry_name.get()
        age = self.entry_age.get()
        gender = self.gender_var.get()
        contact = self.entry_contact.get()
        disease = self.entry_disease.get()
        date = self.entry_date.get()  # Date input

        # Validate input
        if not (name and age and contact and disease and date):
            messagebox.showwarning("Input Error", "Please fill all fields")
            return

        try:
            age = int(age)
        except ValueError:
            messagebox.showerror("Input Error", "Age must be a number")
            return

        try:
            # Validate the date format
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Input Error", "Date format should be YYYY-MM-DD")
            return

        # Insert data into the database
        self.cursor.execute("INSERT INTO patients (name, age, gender, contact, disease, date) VALUES (?, ?, ?, ?, ?, ?)",
                            (name, age, gender, contact, disease, date))
        self.conn.commit()

        messagebox.showinfo("Success", "Data saved successfully!")
        self.clear_data()

    def clear_data(self):
        """Clears the input fields."""
        self.entry_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_contact.delete(0, tk.END)
        self.entry_disease.delete(0, tk.END)
        self.entry_date.delete(0, tk.END)
        self.gender_var.set('Male')

    def retrieve_data(self):
        """Retrieves all the patient data from the database and displays it in the TreeView."""
        self.cursor.execute("SELECT * FROM patients")
        rows = self.cursor.fetchall()

        # Clear the TreeView first
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Insert the data into the TreeView
        for row in rows:
            self.tree.insert("", tk.END, values=row)

    def close_db(self):
        """Closes the database connection."""
        self.conn.close()


# Main part of the application
if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()

    # Create an instance of the HospitalDataEntryApp class
    app = HospitalDataEntryApp(root)

    # Run the application
    root.mainloop()

    # Close the database connection when the application is closed
    app.close_db()

###
'''
import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Create/connect to database
conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

# Create a table for storing patient data if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL,
    contact TEXT NOT NULL,
    disease TEXT NOT NULL
)
""")
conn.commit()

# Function to save data into the database
def save_data():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    contact = entry_contact.get()
    disease = entry_disease.get()

    if not (name and age and contact and disease):
        messagebox.showwarning("Input Error", "Please fill all fields")
        return

    try:
        age = int(age)
    except ValueError:
        messagebox.showerror("Input Error", "Age must be a number")
        return

    # Insert data into the database
    cursor.execute("INSERT INTO patients (name, age, gender, contact, disease) VALUES (?, ?, ?, ?, ?)",
                   (name, age, gender, contact, disease))
    conn.commit()

    messagebox.showinfo("Success", "Data saved successfully!")
    clear_data()

# Function to clear form
def clear_data():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_contact.delete(0, tk.END)
    entry_disease.delete(0, tk.END)
    gender_var.set('Male')

# Function to retrieve data from the database
def retrieve_data():
    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()

    # Clear the tree view first
    for row in tree.get_children():
        tree.delete(row)

    # Insert the data into the tree view
    for row in rows:
        tree.insert("", tk.END, values=row)

# GUI Setup
root = tk.Tk()
root.title("Hospital Data Entry Application")

# Patient details frame
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

# Name
tk.Label(frame, text="Patient Name:").grid(row=0, column=0, pady=5)
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1, pady=5)

# Age
tk.Label(frame, text="Age:").grid(row=1, column=0, pady=5)
entry_age = tk.Entry(frame)
entry_age.grid(row=1, column=1, pady=5)

# Gender
tk.Label(frame, text="Gender:").grid(row=2, column=0, pady=5)
gender_var = tk.StringVar(value="Male")
tk.Radiobutton(frame, text="Male", variable=gender_var, value="Male").grid(row=2, column=1, sticky=tk.W)
tk.Radiobutton(frame, text="Female", variable=gender_var, value="Female").grid(row=2, column=2, sticky=tk.W)

# Contact
tk.Label(frame, text="Contact No:").grid(row=3, column=0, pady=5)
entry_contact = tk.Entry(frame)
entry_contact.grid(row=3, column=1, pady=5)

# Disease
tk.Label(frame, text="Disease:").grid(row=4, column=0, pady=5)
entry_disease = tk.Entry(frame)
entry_disease.grid(row=4, column=1, pady=5)

# Save and Clear buttons
save_button = tk.Button(frame, text="Save", command=save_data)
save_button.grid(row=5, column=0, pady=20)

clear_button = tk.Button(frame, text="Clear", command=clear_data)
clear_button.grid(row=5, column=1, pady=20)

# Retrieve Button
retrieve_button = tk.Button(frame, text="Retrieve Data", command=retrieve_data)
retrieve_button.grid(row=6, column=0, pady=10)

# TreeView for displaying retrieved data
columns = ("id", "name", "age", "gender", "contact", "disease")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col.capitalize())
tree.pack(pady=20)

# Start the GUI loop
root.mainloop()

# Close database connection when done
conn.close()
'''
