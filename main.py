from greeting import greeter, filegreeter, jsongreeter

greeter = greeter.Greeter()
file_greeter = filegreeter.FileGreeter("default_greeting.txt")
json_greeter = jsongreeter.JsonGreeter("greetings.json")

greetings = [
    greeter.greet("Barry Scott"),
    file_greeter.greet("James Jarrold"),
    json_greeter.greet("Harry Harbottle")
]

print(greetings)

greetings.append(greeter.greet("barry"))

print(greetings)

print(greetings.__len__(), "greetings on the list")

print(__name__)