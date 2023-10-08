import tkinter as tk
import random
import string

# Function to generate a random password
def generate_password(length, username):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    # Include alphabets from the username
    username_letters = ''.join(filter(str.isalpha, username))
    if len(username_letters) >= 3:
        # Include at least 3 username letters in the password
        for _ in range(3):
            index = random.randint(0, len(username_letters) - 1)
            password = password[:index] + username_letters[random.randint(0, len(username_letters) - 1)] + password[index+1:]
    
    return password

# Function to generate and display a password
def generate_password_and_display():
    try:
        username = username_entry.get()
        length = int(length_entry.get())
        if length <= 0:
            result_label.config(text="Please enter a positive length.", fg="red")
        else:
            password = generate_password(length, username)
            password_display.config(text=password)
            result_label.config(text="Password generated successfully.", fg="green")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid number.", fg="red")

# Function to accept the generated password
def accept_password():
    username = username_entry.get()
    password = password_display.cget("text")
    accepted_password_label.config(text=f"Accepted Password for {username}: {password}", fg="green")

# Function to reject the generated password
def reject_password():
    username = username_entry.get()
    password = password_display.cget("text")
    rejected_password_label.config(text=f"Rejected Password for {username}: {password}", fg="red")

# Function to reset the fields
def reset_fields():
    username_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    password_display.config(text="")
    accepted_password_label.config(text="")
    rejected_password_label.config(text="")
    result_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Set background color and window size
root.configure(bg="#F3F4F6")  # Light gray background
root.geometry("400x350")

# Title label
title_label = tk.Label(root, text="Password Generator", font=("Arial", 20), bg="#F3F4F6")
title_label.pack()

# Label and entry for username
username_label = tk.Label(root, text="Enter your username:", bg="#F3F4F6")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Label and entry for password length
length_label = tk.Label(root, text="Password Length (e.g., 12):", bg="#F3F4F6")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password_and_display, bg="#4CAF50", fg="white")
generate_button.pack()

# Display generated password
password_display = tk.Label(root, text="", font=("Arial", 16), bg="#F3F4F6")
password_display.pack()

# Buttons to accept, reject, and reset
button_frame = tk.Frame(root, bg="#F3F4F6")
accept_button = tk.Button(button_frame, text="Accept", command=accept_password, bg="#4CAF50", fg="white")
reject_button = tk.Button(button_frame, text="Reject", command=reject_password, bg="#F44336", fg="white")
reset_button = tk.Button(button_frame, text="Reset", command=reset_fields, bg="#2196F3", fg="white")
accept_button.pack(side="left")
reject_button.pack(side="left")
reset_button.pack(side="left")
button_frame.pack()

# Labels for accepted and rejected passwords
accepted_password_label = tk.Label(root, text="", font=("Arial", 12), bg="#F3F4F6", fg="green")
rejected_password_label = tk.Label(root, text="", font=("Arial", 12), bg="#F3F4F6", fg="red")
accepted_password_label.pack()
rejected_password_label.pack()

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#F3F4F6")
result_label.pack()

# Run the main loop
root.mainloop()
