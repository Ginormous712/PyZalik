from MediaNote import MediaNote


class AudioNote(MediaNote):
    def __init__(self, title, tags, importance, path, duration):
        super().__init__(title, tags, importance, path)
        self.duration = duration

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        self.__duration = duration

    def update(self, title=None, tags=None, importance=None, path=None, duration=None):
        super().update(title, tags, importance, path)
        if duration is not None:
            self.duration = duration
