dealt1 = ""
dealt2 = ""
dealt3 = ""
ai1 = ""
ai2 = ""
player1 = ""
player2 = ""

def createdeck():
    with open("Poker/deck.txt") as file:
        cards = file.readlines()
        cards = [line.rstrip('\n') for line in cards]
    deck = [[item + " of Diamonds" for item in cards],
            [item + " of Hearts" for item in cards],
            [item + " of Clovers" for item in cards],
            [item + " of Spades" for item in cards]
            ]
    return deck

def first_cards():
    return