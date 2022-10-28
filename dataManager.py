import json

with open("data.json") as file:
    data = json.load(file)

templates = [
    "{noun} {physicalVerbPast} someone!",
    "You are a {adj} {noun} as you have {physicalVerbPast} the {noun}.",
    "I am so {adj}! I did not even see that {noun} coming!",
    "Why aren't you doing something, {name}, are you trying to get us punished by the teacher?",
    "When {name} is doing something he enjoys, he is good, but other times he is bad.",
    "{name} is better than you.",
    "{name} {physicalVerbPast} a {noun}?!",
    "To {physicalVerb} is considered {adj}"
]