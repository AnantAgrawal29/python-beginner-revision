#TODO: Create a letter using starting_letter.txt

with open("Input/Letters/starting_letter.txt") as file:
    letter  = file.read()

#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.

with open("Input/Names/invited_names.txt") as file:
    names = file.read()
names = names.split('\n')

#Save the letters in the folder "ReadyToSend".
for name in names:
    letter_name = letter.replace('[name]',name)
    with open(f"Output/ReadyToSend/{name}.txt", 'w') as file:
        file.write(letter_name)
