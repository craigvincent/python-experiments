from kindness.friendly import greeter
from kindness.friendly.greetingreader import GreetingReader

greetings = [
    greeter.say_hello("Craig", "Blimey guv, absolute pleasure to meet your aquaintance"),
    greeter.say_hello("Nick"),
    greeter.say_hello("Bob"),
    greeter.say_hello("Geoff S", "Yo"),
    greeter.say_hello_from_file("Barry Scott")
]

print(greetings)

greetings.append(greeter.say_hello("barry"))

print(greetings)

print(greetings.__len__(), "greetings on the list")

print(__name__)

gr = GreetingReader('greetings.json')
print(gr.get_random())
