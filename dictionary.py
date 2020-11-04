import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        # data.keys() is a method in get_close_matches return list of the closest keys in the dictionary

        yes_or_no = input("Did you mean %s instead? Enter y if yes, or n if no: " % get_close_matches(w, data.keys())[0])
        # %s make variable of (s) which equal the sentence after the next % like formating the string
        if yes_or_no == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yes_or_no == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word does not exist , please double check it."
word = input("Enter a word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
