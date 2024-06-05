from Note import Note


class MediaNote(Note):
    def __init__(self, title, tags, importance, path):
        super().__init__(title, tags, importance)
        self.path = path

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, value):
        self.__path = value

    def update(self, title=None, tags=None, importance=None, path=None):
        super().update(title, tags, importance)
        if path is not None:
            self.path = path