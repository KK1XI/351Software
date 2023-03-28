class Project:
    def __init__(self, uid, name, description, progress, dueDate):
        self.uid = uid
        self.name = name
        self.description = description
        self.progress = progress
        self.dueDate = dueDate

    def update(self, uid, name, description, progress, dueDate):
        self.uid = uid
        self.name = name
        self.description = description
        self.progress = progress
        self.dueDate = dueDate
