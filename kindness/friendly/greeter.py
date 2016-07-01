def say_hello(name, greeting="Hello") -> str:
    return greeting + " " + name


def say_hello_from_file(name, greeting_file="default_greeting.txt") -> str:
    greeting = ''
    with open(greeting_file, 'r') as f:
        greeting = f.read()
    return say_hello(name, greeting)
