import json


class Config:
    def __init__(self, path="config.json"):
        self.path = path
        self.config = {}
        self.load()

    def load(self):
        with open(self.path, "r", encoding="utf-8") as f:
            self.config = json.load(f)

    def save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=4)
