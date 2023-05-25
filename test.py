
import json
import pickle
import csv
import os
from datetime import datetime

class Note:
    def __init__(self, id, title, body, created_at, updated_at):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = created_at
        self.updated_at = updated_at

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }     


class NoteManager:
    def __init__(self, filename):
        self.filename = filename
        self.notes = self.load_notes(self.filename)

    def create_note(self, title, body):
        print(self.notes)
        if self.notes == None:
            self.notes = []
            note_id = 1
        else:
            note_id = len(self.notes) + 1
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        updated_at = created_at
        note = Note(note_id, title, body, created_at, updated_at)
        self.notes.append(note)
        self.save_notes(self.filename)

    def read_notes(self):
        for note in self.notes:
            print(f"ID: {note.get_id()}")
            print(f"Title: {note.get_title()}")
            print(f"Body: {note.body}")
            print(f"Created at: {note.created_at}")
            print(f"Updated at: {note.updated_at}")
            print()

    def edit_note(self, note_id, new_title, new_body):
        for note in self.notes:
            if note.get_id() == note_id:
                note.set_title(new_title)
                note.body = new_body
                note.updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save_notes(self.filename)
                return

        print("Note not found.")

    def save_notes(self, file_name):
        with open(file_name, 'wb') as file:
            pickle.dump(self.notes, file)

    def load_notes(self, file_name):
        if os.path.getsize(file_name) > 0:
            with open(file_name, 'rb') as file:
                self.notes = pickle.load(file)

    def delete_note(self, index):
        if index < 0 or index >= len(self.notes):
            print("Некорректный индекс заметки.")
            return

        del self.notes[index]

print("Программа запущена")
manager = NoteManager('notes.pickle')
manager.create_note('Note 1', 'Пака номер 1')
manager.create_note('Note 2', 'Папка номер 2')
manager.save_notes('notes.pickle')
manager.load_notes('notes.pickle')
manager.read_notes()
manager.edit_note(0, 'Edited note title', 'New content')
manager.delete_note(1)
manager.read_notes()
manager.save_notes('notes.pickle')
print("Реузльтат:","Проведена работа с заметками!")