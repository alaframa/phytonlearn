import tkinter as tk

# Define a function to handle button clicks
def button_click(value):
    print(f"Button clicked: {value}")

# Create the main application window
root = tk.Tk()
root.title("Calculator")

# Create buttons using a nested loop
buttons = [
    ["1", "2", "3", "+"],
    ["4", "5", "6", "-"],
    ["7", "8", "9", "x"],
    ["0", "--", "=", "/"]
]

for i, row in enumerate(buttons):
    for j, value in enumerate(row):
        # Create a button with the corresponding value
        button = tk.Button(root, text=value, width=5, height=2,
                           command=lambda v=value: button_click(v))
        # Use grid geometry manager to position the button
        button.grid(row=i, column=j, padx=5, pady=5)

# Start the GUI event loop
root.mainloop()
