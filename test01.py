import os
import pickle

class Note:
    def init(self, title, content):
        self.title = title
        self.content = content

class NoteManager:
    def init(self, filename):
        self.filename = filename
        self.notes = []
        self.load_notes()

    def load_notes(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as file:
                self.notes = pickle.load(file)

    def save_notes(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.notes, file)

    def create_note(self, title, content):
        note = Note(title, content)
        self.notes.append(note)
        self.save_notes()

    def read_notes(self):
        if not self.notes:
            print("Нет доступных заметок.")
            return

        for index, note in enumerate(self.notes):
            print(f"Заметка {index+1}:")
            print(f"Заголовок: {note.title}")
            print(f"Содержимое: {note.content}")
            print()

    def edit_note(self, index, title, content):
        if index < 0 or index >= len(self.notes):
            print("Неверный индекс заметки.")
            return

        note = self.notes[index]
        note.title = title
        note.content = content
        self.save_notes()

    def delete_note(self, index):
        if index < 0 or index >= len(self.notes):
            print("Неверный индекс заметки.")
            return

        del self.notes[index]
        self.save_notes()

        print("Программа запущена")
manager = NoteManager("notes.pickle")
manager.create_note("Заметка 1", "Это содержимое заметки 1")
manager.create_note("Заметка 2", "Это содержимое заметки 2")
manager.read_notes()
manager.edit_note(0, "Измененная заметка 1", "Новое содержимое заметки 1")
manager.delete_note(1)
manager.read_notes()

