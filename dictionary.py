import json
data = json.load(open("data.json"))
def translate(w):
    if w in data:
        return data[w]
    else :
        return "The word does not exist , please double check it."
word = input("Enter a word: ")
print (translate(word))
