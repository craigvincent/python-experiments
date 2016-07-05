from greeting.greeter import Greeter


class FileGreeter(Greeter):
    greeting_file = ""
    greetings = ""

    def __init__(self, greeting_file):
        self.greeting_file = greeting_file
        self.load()
        return

    def load(self):
        with open(self.greeting_file, 'r') as f:
            self.greeting = f.read()

    def get_salutation(self):
        return self.greeting
