import json
import random

from greeting.filegreeter import FileGreeter


class JsonGreeter(FileGreeter):
    greetings = []

    def load(self):
        with open(self.greeting_file, 'r') as f:
            new_greetings = json.load(f)
            self.greetings.clear()
            for n in new_greetings:
                self.greetings.append(n)

    def get_salutation(self):
        return random.choice(self.greetings)
