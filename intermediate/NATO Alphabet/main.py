import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabets = {row.letter: row.code for (index,row) in data.iterrows()}
print(nato_alphabets)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

while True:
    try:
        word = input("Enter a word: ").upper()
        phonetic_code = [nato_alphabets[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        break
print(phonetic_code)