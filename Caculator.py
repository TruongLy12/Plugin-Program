import tkinter as tk
from tkinter import ttk
import execjs

# Load the JavaScript file
with open("plugin.js", "r") as file:
    js_code = file.read()

# Initialize PyExecJS context
ctx = execjs.compile(js_code)

def calculate_addition():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

def calculate_subtraction():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        # Call javascript function to execute the subtraction 
        result = ctx.call("subtract", num1, num2)
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

def calculate_multiplication():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        # Call javascript function to execute the multiplication 
        result = ctx.call("multiply", num1, num2)
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Addition Calculator")
root.geometry("500x400")
root.resizable(False, False)

# Style configuration
style = ttk.Style()
style.configure("TButton", padding=10, font=("Helvetica", 20))
style.configure("TEntry", padding=10, font=("Helvetica", 20))
style.configure("TLabel", font=("Helvetica", 12))

# Create input fields
label1 = ttk.Label(root, text="Enter first number:")
label1.pack(pady=5)
entry1 = ttk.Entry(root)
entry1.pack(pady=5)

label2 = ttk.Label(root, text="Enter second number:")
label2.pack(pady=5)
entry2 = ttk.Entry(root)
entry2.pack(pady=5)


# Create the button for addition
add_button = tk.Button(root, text="Add", command=calculate_addition)
add_button.pack(pady=10)

# Create the button for subtraction
subtract_button = tk.Button(root, text="Subtract", command=calculate_subtraction)
subtract_button.pack(pady=10)

# Create the button for multiplication
multiply_button = tk.Button(root, text="Multiply", command=calculate_multiplication)
multiply_button.pack(pady=10)

# Display the result
result_label = ttk.Label(root, text="", foreground="green")
result_label.pack()

# Run the Tkinter event loop
root.mainloop()
