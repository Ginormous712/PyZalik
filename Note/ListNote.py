from Note import Note


class ListNote(Note):
    def __init__(self, title, tags, importance, list_x):
        super().__init__(title, tags, importance)
        self.list_x = list_x

    @property
    def list_x(self):
        return self._list_x

    @list_x.setter
    def list_x(self, value):
        self._list_x = value

    def update(self, title=None, tags=None, importance=None, list_x=None):
        super().update(title, tags, importance)
        if list_x is not None:
            self.list_x = list_x
