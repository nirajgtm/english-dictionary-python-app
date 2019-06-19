import	json
from difflib import get_close_matches #Library to compare text
data = json.load(open("dictionary-file.json"))

def meaning(word):
	if word in data:
		for value in data[word]:
			 return value
			 print("\n")
		
	elif get_close_matches(word, data.keys(), cutoff=0.6) !=  []:
		matches = get_close_matches(word, data.keys(), cutoff=0.6)
		return("Words Does not Exist! \n Closest match is: '{0}'" .format(matches[0]))
	else :
		return("Please check your word, it doesn't make any sense")

word = input ("Enter the word: ")

print(meaning(word.lower()))
