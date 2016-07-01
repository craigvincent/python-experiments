import json
import random


class GreetingReader:
    greetings = []

    def __init__(self, filename):
        self.load(filename)

    def load(self, filename):
        with open(filename, 'r') as f:
            new_greetings = json.load(f)
            self.greetings.clear()
            for n in new_greetings:
                self.greetings.append(n)

    def get_random(self):
        return random.choice(self.greetings)

    def get_specific(self, i):
        return self.greetings[i]
