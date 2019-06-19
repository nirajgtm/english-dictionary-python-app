import	json
data = json.load(open("dictionary-file.json"))

def meaning(word):
	if word in data:
		return data[word]
	else:
		print("incorrect word bitch")

word = input ("Enter the word: ")

print(meaning(word.lower()))
