import tkinter as tk
from tkinter import ttk

# Function to add a new note (Placeholder for actual functionality)
def add_note():
    pass  # Implement the function to add a new note here

# Function to delete a selected note (Placeholder for actual functionality)
def delete_note():
    pass  # Implement the function to delete a note here

# Function to save notes (Placeholder for actual functionality)
def save_notes():
    pass  # Implement the function to save notes here

# Create the main window
root = tk.Tk()
root.title("SimpleNotes")

# Create a frame for the treeview (scrollable table)
tree_frame = tk.Frame(root)
tree_frame.pack(fill=tk.BOTH, expand=True)

# Create the treeview
tree = ttk.Treeview(tree_frame, columns=('Notes', 'Dates'), show='headings')
tree.heading('Notes', text='Notes')
tree.heading('Dates', text='Date')
tree.column('Notes', stretch=tk.YES)
tree.column('Dates', width=100)

# Add a scrollbar
scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(fill=tk.X)

# Add buttons
add_button = tk.Button(button_frame, text="Add Note", command=add_note)
add_button.pack(side=tk.LEFT, padx=5, pady=5)

delete_button = tk.Button(button_frame, text="Delete", command=delete_note)
delete_button.pack(side=tk.LEFT, padx=5, pady=5)

save_button = tk.Button(button_frame, text="Save", command=save_notes)
save_button.pack(side=tk.LEFT, padx=5, pady=5)

# Start the application
root.mainloop()
