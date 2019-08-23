import json
from difflib import get_close_matches
data=json.load(open("dictionary.json"))

def translate(m):
    m=m.lower()
    if m in data:
        return data[m]
    elif len(get_close_matches(m,data.keys())) >0:
        Mn = input("did you mean %s instead? Enter Y if yes, or N if no: " %get_close_matches(m,data.keys())[0])
        if Mn == "Y":
            return data[get_close_matches(m,data.keys())[0]]
        else:
            return "we didn't understand your entry."
    else:
        print("the word not present,please check again")

word = input("enter word: ")

print(translate(word))