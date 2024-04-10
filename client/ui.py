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
    # Clear existing treeview
    tree.delete(*tree.get_children())
    
    # Get notes from NoteManager
    notes = note_manager.get_notes()  # No arguments should be passed here
    
    # Insert notes into treeview
    for note in notes:
        # Assuming each note is a tuple of (note_text, timestamp)
        # You might need to adjust this based on the actual structure of your notes
        tree.insert('', 'end', values=note)

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
sync_button = tk.Button(button_frame, text="Sync", command=note_manager.sync)
sync_button.pack(side=tk.LEFT, padx=5, pady=5)

add_button = tk.Button(button_frame, text="Add Note", command=add_note)
add_button.pack(side=tk.LEFT, padx=5, pady=5)

# Start the application
root.mainloop()