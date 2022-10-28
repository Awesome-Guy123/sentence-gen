from random import choice
from dataManager import data, templates



def generateNewSentence():
    return choice(templates).format(noun=choice(data["nouns"]), adj=choice(data["adjectives"]), physicalVerbPast=choice(data["verbs"]["physicalVerbs"]["pastTense"]), physicalVerb=choice(data["verbs"]["physicalVerbs"]["presentTense"]),name=choice(data["names"]))


if __name__ == "__main__":
    for _ in range(100):
        print(generateNewSentence())