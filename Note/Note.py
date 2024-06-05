from datetime import datetime


class Note:
    def __init__(self, title, tags, importance):
        self.title = title
        self.tags = tags
        self.importance = importance
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def tags(self):
        return self.__tags

    @tags.setter
    def tags(self, tags):
        self.__tags = tags

    @property
    def importance(self):
        return self.__importance

    @importance.setter
    def importance(self, importance):
        self.__importance = importance

    @property
    def updated_at(self):
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, value):
        self.__updated_at = value

    def update(self, title=None, tags=None, importance=None):
        if title is not None:
            self.title = title
        if tags is not None:
            self.tags = tags
        if importance is not None:
            self.importance = importance
        self.updated_at = datetime.now()



