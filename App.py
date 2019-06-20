import	json
from difflib import get_close_matches #Library to compare text
data = json.load(open("dictionary-file.json"))

def meaning(word):

	novalue = "Please check your word, it doesn't make any sense"
	if word in data:
		return data[word]

	elif word.capitalize() in data:
		return data[word.capitalize()]

	elif word.upper() in data:
		return data[word.upper()]

		
	elif get_close_matches(word, data.keys(), cutoff=0.6) !=  []:
		match = get_close_matches(word, data.keys(), cutoff=0.6)
		userinput = input("Did you mean'{0}' instead ? (Y/N)" .format(match[0]))
		if userinput.lower() == "y"  :
			return data[match[0]]
		elif userinput.lower() == "n"  :
			if match[1] :
				userinput = input("Did you mean'{0}' instead ? (Y/N)" .format(match[1]))
				if userinput.lower() == "y"  :
					return data[match[1]]
				else:
					return(novalue)

			else:
				return(novalue)
		else:
			return(novalue)

	else :
		return(novalue)

word = input ("Enter the word: ")

result = meaning(word.lower())

if type(result) == list:
	for meanings in result:
		print( "-- " + meanings)
else:
	print (result) 