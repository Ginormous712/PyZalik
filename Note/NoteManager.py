from Note import *

'''Can also add variable max_importance and method 
    to set note to the top (set its importance to max + 1, max++), 
    but no need in this implementation'''


class NoteManager:
    def __init__(self):
        self.__notes = []

    @property
    def notes(self):
        return self.__notes

    @notes.setter
    def notes(self, notes):
        self.__notes = notes

    def create(self, note):
        self.notes.append(note)

    # By title
    def read(self, title):
        for note in self.notes:
            if note.title == title:
                return note
        return None

    # By title
    def update(self, title, **kwargs):
        for note in self.notes:
            if note.title == title:
                note.update(**kwargs)

    def delete(self, title):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)

    def search_by_class(self, class_name):
        return [note for note in self.notes if isinstance(note, class_name)]

    def search_by_date_range(self, start_date, end_date):
        return [note for note in self.notes if start_date <= note.updated_at <= end_date]

    '''We find intersection between 2 sets: tags of every Note and given tags. 
    As a result we get Note if at least 1 of tags is in both sets'''
    def search_by_tags(self, tags):
        return [note for note in self.notes if set(tags).intersection(set(note.tags))]

    def sort_notes(self, by):
        if by == 'title':
            return sorted(self.notes, key=lambda x: x.title)
        elif by == 'importance':
            return sorted(self.notes, key=lambda x: x.importance, reverse=True)
        elif by == 'updated_at':
            return sorted(self.notes, key=lambda x: x.updated_at, reverse=True)
        else:
            raise ValueError("Invalid sorting criteria")
