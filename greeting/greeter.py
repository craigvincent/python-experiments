class Greeter:
    def greet(self, name):
        return self.get_salutation() + " " + name

    def get_salutation(self):
        return "Hello"
