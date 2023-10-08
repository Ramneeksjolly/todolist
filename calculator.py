import tkinter as tk
import math

# Function to calculate square root
def square_root():
    try:
        num = float(entry_expression.get())
        result = math.sqrt(num)
        entry_result.delete(0, tk.END)
        entry_result.insert(0, result)
    except Exception as e:
        entry_result.delete(0, tk.END)
        entry_result.insert(0, "Error")

# Function to clear the input fields
def clear_input():
    entry_expression.delete(0, tk.END)
    entry_result.delete(0, tk.END)

# Function to perform arithmetic operations
def calculate():
    try:
        expression = entry_expression.get()
        result = eval(expression)
        entry_result.delete(0, tk.END)
        entry_result.insert(0, result)
    except Exception as e:
        entry_result.delete(0, tk.END)
        entry_result.insert(0, "Error")

# Function to add a character to the expression field
def add_to_expression(char):
    current_expression = entry_expression.get()
    entry_expression.delete(0, tk.END)
    entry_expression.insert(0, current_expression + char)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Set window size and background color
root.geometry("400x500")
root.configure(bg="#F3F4F6")  # Light gray background

# Expression field
entry_expression = tk.Entry(root, font=("Arial", 24))
entry_expression.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Result field
entry_result = tk.Entry(root, font=("Arial", 24))
entry_result.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Create a 5x4 grid for buttons
button_frame = tk.Frame(root, bg="#F3F4F6")
button_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Button labels for numbers and operations
button_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C', '√'
]

# Function to handle button clicks
def button_click(char):
    if char == '=':
        calculate()
    elif char == 'C':
        clear_input()
    elif char == '√':
        square_root()
    else:
        add_to_expression(char)

# Create buttons
row, col = 0, 0
for label in button_labels:
    button = tk.Button(button_frame, text=label, font=("Arial", 16), command=lambda label=label: button_click(label))
    button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
    col += 1
    if col > 3:
        col = 0
        row += 1

# Configure grid to expand buttons when the window is resized
for i in range(5):
    button_frame.columnconfigure(i, weight=1)
    button_frame.rowconfigure(i, weight=1)

# Run the main loop
root.mainloop()
