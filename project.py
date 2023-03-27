class Project:
    def __init__(self, name, description, progress):
        self.name = name
        self.description = description
        self.progress = progress

    def update(self, name, description, progress):
        self.name = name
        self.description = description
        self.progress = progress
