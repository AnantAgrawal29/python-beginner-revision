import random
def drawCard(cards):
    cards.append(random.randint(2,11))
    if (11 in cards) and sum(cards)>21:
        cards.remove(11) 
        cards.append(1)

def blackjack(cards, computerCards):
    totpl = sum(cards)
    totcomp = sum(computerCards)

    print(f"\tYour final hand: {cards}, final score {totpl}")
    print(f"\tComputer's final hand: {computerCards}, final score: {totcomp}")

    if (totpl==totcomp) or (totcomp==21 and totpl==21):
        print("Draw 🙃")
    elif totpl==21 and len(cards)==2:
        print("Win with a Blackjack 😎")
    elif totcomp==21 and len(computerCards)==2:
        print("Lose, Opponent has a Blackjack 😱")
    elif totcomp > 21:
        print("Opponent went over. You win 😃")
    elif totpl > totcomp:
        print("You win 😃")
    elif totpl < totcomp:
        print("You lose 😤")

while True:
    ch = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if ch=='n':
        break
    print(r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
    |  \/ K|                            _/ |                
    '------'                           |__/           """)
    
    computer_total=0
    player_total=0
    choice='y'
    player_cards=[]
    comp_cards = []

    drawCard(player_cards)
    drawCard(player_cards)

    while sum(comp_cards) < 17:
        drawCard(comp_cards)

    while choice=='y':
        print(f"\tYour cards: {player_cards}, current score {sum(player_cards)}")
        print(f"\tComputer's first card: {comp_cards[0]}")
        if sum(player_cards) > 21:
            print(f"\tYour final hand: {player_cards}, final score {sum(player_cards)}")
            print(f"\tComputer's final hand: {comp_cards}, final score: {sum(comp_cards)}")
            print("You went over. You lose 😭")
            break
        choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if choice == 'y':
            drawCard(player_cards)
        else:
            blackjack(player_cards, comp_cards)