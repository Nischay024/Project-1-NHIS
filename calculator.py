import tkinter as tk
import math


def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)


def clear():
    entry.delete(0, tk.END)
 

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to calculate percentage
def percentage():
    try:
        current = entry.get()
        result = str(float(current) / 100)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to calculate square root
def square_root():
    try:
        current = entry.get()
        result = str(math.sqrt(float(current)))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to handle backspace
def backspace():
    current = entry.get()
    entry.delete(len(current)-1, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the entry field
entry = tk.Entry(root, width=20, font=('Arial', 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Buttons for the calculator with colors
buttons = [
    ('7', 1, 0, '#f0f0f0'), ('8', 1, 1, '#f0f0f0'), ('9', 1, 2, '#f0f0f0'), ('/', 1, 3, '#4CAF50'),
    ('4', 2, 0, '#f0f0f0'), ('5', 2, 1, '#f0f0f0'), ('6', 2, 2, '#f0f0f0'), ('*', 2, 3, '#4CAF50'),
    ('1', 3, 0, '#f0f0f0'), ('2', 3, 1, '#f0f0f0'), ('3', 3, 2, '#f0f0f0'), ('-', 3, 3, '#4CAF50'),
    ('0', 4, 0, '#f0f0f0'), ('.', 4, 1, '#f0f0f0'), ('+', 4, 2, '#4CAF50'), ('=', 4, 3, '#2196F3'),
    ('C', 5, 0, '#F44336'), ('√', 5, 1, '#FF9800'), ('%', 5, 2, '#FFEB3B'), ('←', 5, 3, '#FF5722')
]

# Create and place buttons dynamically
for (text, row, col, color) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=evaluate, bg=color)
    elif text == 'C':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=clear, bg=color)
    elif text == '√':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=square_root, bg=color)
    elif text == '%':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=percentage, bg=color)
    elif text == '←':
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=backspace, bg=color)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=lambda t=text: button_click(t), bg=color)
    
    button.grid(row=row, column=col, padx=5, pady=5)

# Run the main loop
root.mainloop()