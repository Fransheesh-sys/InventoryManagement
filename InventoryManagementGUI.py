import tkinter as tk
from tkinter import messagebox

# Predefined credentials
valid_username = "Francis"
valid_password = "Jumamoy"

# Inventory dictionary
inventory = {}


# Function to handle login
def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == valid_username and password == valid_password:
        messagebox.showinfo("Login Successful", f"Welcome {username}!")
        show_inventory_screen()  # Show the inventory screen after successful login
    else:
        messagebox.showwarning("Login Failed", "Invalid Username or Password")


# Function to show inventory screen
def show_inventory_screen():
    # Hide the login frame
    login_frame.pack_forget()

    # Show the inventory management frame
    inventory_frame.pack(fill="both", expand=True)


# Function to log out and return to the login screen
def logout():
    inventory_frame.pack_forget()
    login_frame.pack()


# Inventory management functions
def view_inventory():
    inventory_list.delete(0, tk.END)  # Clear the listbox
    if inventory:
        for item, quantity in inventory.items():
            inventory_list.insert(tk.END, f"{item}: {quantity}")
    else:
        inventory_list.insert(tk.END, "The inventory is empty.")


def add_item():
    item = entry_item.get()
    try:
        quantity = int(entry_quantity.get())
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number for quantity.")
        return

    if item:
        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity
        messagebox.showinfo("Item Added", f"{quantity} of {item} added to the inventory.")
        entry_item.delete(0, tk.END)
        entry_quantity.delete(0, tk.END)
        view_inventory()
    else:
        messagebox.showwarning("Input Error", "Please enter an item name.")


def remove_item():
    item = entry_item.get()
    try:
        quantity = int(entry_quantity.get())
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number for quantity.")
        return

    if item in inventory:
        if inventory[item] >= quantity:
            inventory[item] -= quantity
            if inventory[item] == 0:
                del inventory[item]
            messagebox.showinfo("Item Removed", f"{quantity} of {item} removed from the inventory.")
            entry_item.delete(0, tk.END)
            entry_quantity.delete(0, tk.END)
            view_inventory()
        else:
            messagebox.showwarning("Not Enough Stock", f"Cannot remove {quantity}. Current stock is {inventory[item]}.")
    else:
        messagebox.showwarning("Item Not Found", f"{item} not found in the inventory.")


# Create the main window
window = tk.Tk()
window.title("Inventory Management")
window.geometry("500x500")
window.config(bg="#1877F2")

# Login Frame
login_frame = tk.Frame(window, bg="#000080", padx=20, pady=20)

label_title = tk.Label(login_frame, text="Welcome User", font=("Arial", 20, "bold"), bg="#000080",
                       fg="#FFFFFF")
label_title.pack(pady=20)

login_container = tk.Frame(login_frame, bg="#FFFFFF", padx=40, pady=40, relief="solid", bd=1)
login_container.pack()

label_username = tk.Label(login_container, text="Username", font=("Arial", 12), bg="#FFFFFF", fg="#1C1E21")
label_username.pack(pady=5)

entry_username = tk.Entry(login_container, font=("Arial", 12), relief="solid", bd=1)
entry_username.pack(pady=5)

label_password = tk.Label(login_container, text="Password", font=("Arial", 12), bg="#FFFFFF", fg="#1C1E21")
label_password.pack(pady=5)

entry_password = tk.Entry(login_container, show="*", font=("Arial", 12), relief="solid", bd=1)
entry_password.pack(pady=5)

login_button = tk.Button(login_container, text="Login", font=("Helvetica", 12), bg="#00FF00", fg="white", relief="flat",
                         command=login)
login_button.pack(pady=20)

login_frame.pack()

# Inventory Frame
inventory_frame = tk.Frame(window, bg="#1A1A4B", padx=20, pady=20)

# Inventory widgets
label_welcome = tk.Label(inventory_frame, text="Inventory Management", font=("Helvetica", 16, "bold"), bg="#1A1A4B",
                         fg="#1877F2")
label_welcome.pack(pady=10)

inventory_container = tk.Frame(inventory_frame, bg="#ADD8E6", padx=20, pady=20, relief="solid", bd=1)
inventory_container.pack()

label_item = tk.Label(inventory_container, text="Item Name", font=("Arial", 12), bg="#FFFFFF", fg="#1C1E21")
label_item.pack(pady=5)

entry_item = tk.Entry(inventory_container, font=("Helvetica", 12), relief="solid", bd=1)
entry_item.pack(pady=5)

label_quantity = tk.Label(inventory_container, text="Quantity", font=("Helvetica", 12), bg="#FFFFFF", fg="#1C1E21")
label_quantity.pack(pady=5)

entry_quantity = tk.Entry(inventory_container, font=("Helvetica", 12), relief="solid", bd=1)
entry_quantity.pack(pady=5)

# Buttons for adding, removing items, and viewing inventory
button_frame = tk.Frame(inventory_container, bg="#FFFFFF")
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Item", font=("Helvetica", 12), bg="#1877F2", fg="white", relief="flat",
                       command=add_item)
add_button.pack(side="left", padx=10)

remove_button = tk.Button(button_frame, text="Remove this Item", font=("Helvetica", 12), bg="#FF6347", fg="white",
                          relief="flat", command=remove_item)
remove_button.pack(side="left", padx=10)

inventory_list = tk.Listbox(inventory_container, height=10, width=40, font=("Helvetica", 12))
inventory_list.pack(pady=10)

# Logout button
logout_button = tk.Button(inventory_container, text="Logout", font=("Helvetica", 12), bg="#FF8C00", fg="white",
                          relief="flat", command=logout)
logout_button.pack(pady=10)

# Show the login screen initially
login_frame.pack()

# Start the main GUI loop
window.mainloop()
