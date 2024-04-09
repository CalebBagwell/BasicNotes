import datetime
from server import *

class NoteManager:
    #Handles note-taking logic, including saving and reading notes.

    def __init__(self, filename="notes.txt"):
        #Initialize the NoteManager with a file to store the notes.
        self.filename = filename
        self.notes = []

    def sync(self):
        # Sync the notes.txt file with the server by overwriting the one stored on the server.
        print("This button does nothing!") 

    def get_notes(self):
        with open('notes.txt', 'r') as f:
            notes = f.readlines()

        note_list = []
        for note in notes:
            if "] " in note:  # Check if the note is in the correct format
                timestamp, note_text = note.strip().split("] ")
                note_list.append((note_text, timestamp[1:]))
            else:
                print(f"Skipping note '{note.strip()}' because it's not in the correct format.")
        return note_list

    def add_note(self, note):
        #Add a note with a timestamp to the file.
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_note = f"[{timestamp}] {note}\n"
        with open(self.filename, "a") as file:
            file.write(formatted_note)
        print("Note added successfully.")
        self.notes.append(note)

    def display_notes(self):
        #Displays the notes stored in the file specified by `self.filename`.
        #Reads the contents of the file line by line and prints each note to the console.
        with open(self.filename, "r") as file:
            notes = file.readlines()
        for note in notes:
            print(note, end='')
        
class CLI:
    #Handles the Command Line Interface for interacting with the user.
    
    def __init__(self, note_manager):
        #Initialize the CLI with a NoteManager instance.
        self.note_manager = note_manager

    def prompt_user(self):
        #Prompt the user for action: take a note, display notes, or exit.
        while True:
            print("\n1. Take a note\n2. Display notes\n3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                note = input("Enter your note: ")
                self.note_manager.add_note(note)
            elif choice == '2':
                self.note_manager.display_notes()
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    #note_manager = NoteManager()
    #cli = CLI(note_manager)
    #cli.prompt_user()
    
    server()
