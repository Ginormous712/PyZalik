from MediaNote import MediaNote


class ImageNote(MediaNote):
    def __init__(self, title, tags, importance, path, size):
        super().__init__(title, tags, importance, path)
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    def update(self, title=None, tags=None, importance=None, path=None, size=None):
        super().update(title, tags, importance, path)
        if size is not None:
            self.size = size
