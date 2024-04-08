import tkinter as tk
from tkinter import simpledialog
from tkinter import ttk
from main import NoteManager

# Create an instance of NoteManager
note_manager = NoteManager()

# Function to add a new note
def add_note():
    # Open a simpledialog box to take the user's note
    note = simpledialog.askstring("Add Note", "Enter your note:")
    if note:
        note_manager.add_note(note)
        refresh_notes()

def refresh_notes():
    # Refreshes the notes displayed in the treeview widget.
    # This function clears the existing notes in the treeview widget and retrieves the latest notes from the note manager.
    # It then inserts each note into the treeview widget.

    tree.delete(*tree.get_children())
    notes = note_manager.get_notes()
    for note in notes:
        note_text, note_date = note  # Unpack the tuple
        tree.insert('', 'end', values=(note_text, note_date))

# Create the main window
root = tk.Tk()
root.title("BasicNotes")

# Create a frame for the treeview (scrollable table)
tree_frame = tk.Frame(root)
tree_frame.pack(fill=tk.BOTH, expand=True)

# Create the treeview
tree = ttk.Treeview(tree_frame, columns=('Notes', 'Date'), show='headings')
tree.heading('Notes', text='Notes')
tree.heading('Date', text='Date')
tree.column('Date', stretch=tk.YES)
tree.column('Notes', stretch=tk.YES)

# Add a scrollbar
scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

refresh_notes()
# Refresh the notes display
# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(fill=tk.X)

# Add buttons
add_button = tk.Button(button_frame, text="Add Note", command=add_note)
add_button.pack(side=tk.LEFT, padx=5, pady=5)

# Start the application
root.mainloop()