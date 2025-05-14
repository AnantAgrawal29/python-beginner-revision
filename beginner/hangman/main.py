import random
from hangman_art import stages, logo1
from hangman_words import word_list

def replace_blank(guess):
    f=False
    for w in range(len(word)):
        if word[w] == guess:
            dash[w] = guess
            f=True
    return f

print(logo1)

word  = list(random.choice(word_list))
dash = list(len(word)*'_')

chances=0
win=False
print(word)
while chances<=5:
    print("Word to guess:",''.join(dash))
    guess = input("\nGuess a guess: ").lower()
    if guess in dash:
        print("You already guessed",guess)
    elif not replace_blank(guess):
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        chances+=1
    if '_' not in dash:
        win=True
        break
    else:
        print(stages[6-chances])
        print(f"****************************{6-(chances)}/6 LIVES LEFT****************************")

if not win:
    print(f"***********************IT WAS {''.join(word)}! YOU LOSE**********************")
else:
    print("".join(dash),"\nYou win")
