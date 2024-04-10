import datetime
import socket
import os

class NoteManager:
    #Handles note-taking logic, including saving and reading notes.

    def __init__(self, filename="notes.txt"):
        #Initialize the NoteManager with a file to store the notes.
        self.filename = filename
        self.notes = []

    def sync(self):
        # Sync the notes.txt file with the server by sending its contents to the server.
        s = socket.socket()
        host = socket.gethostname()  # or '127.0.0.1' for local testing
        port = 3333
        s.connect((host, port))

        # Check if notes.txt exists and send its contents
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                notes = f.read()
                s.send(notes.encode())
        else:
            print("No notes to sync.")
            s.send("".encode())

        # Wait for a response from the server
        response = s.recv(1024).decode()
        print(f"Server response: {response}")

        # Close the connection
        s.close()

    def get_notes(self):
        #Retrieves the notes from the 'notes.txt' file and returns them as a list of tuples.
        #Each tuple in the list contains the note text and its corresponding timestamp.
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

# Example usage
if __name__ == "__main__":
    manager = NoteManager()
    manager.add_note("Test note")
    manager.sync()
