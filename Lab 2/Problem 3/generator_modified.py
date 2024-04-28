import random

def getWords(file_name):
    words = list()
    with open(file_name, 'r') as file:
        for line in file:
            words.append(line.strip())

    return tuple(words)

def sentence():
    return nounPhrase() + " " + verbPhrase()
def nounPhrase():
    return random.choice(articles) + " " + random.choice(nouns)
def verbPhrase():
    return random.choice(verbs) + " " + nounPhrase() + " " + \
        prepositionalPhrase()
def prepositionalPhrase():
    return random.choice(prepositions) + " " + nounPhrase()

nouns = getWords("nouns.txt")
verbs = getWords("verbs.txt")
prepositions = getWords("prepositions.txt")
articles = getWords("articles.txt")

def main():
    #No. of sentences
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())


if __name__ == "__main__":
    main()
