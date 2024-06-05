from Note import Note


class TextNote(Note):
    def __init__(self, title, tags, importance, text):
        super().__init__(title, tags, importance)
        self.text = text

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    def update(self, title=None, tags=None, importance=None, text=None):
        super().update(title, tags, importance)
        if text is not None:
            self.text = text
