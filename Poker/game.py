dealt1 = ""
dealt2 = ""
dealt3 = ""
ai1 = ""
ai2 = ""
player1 = ""
player2 = ""

def createdeck():
    global deck
    with open("Poker/deck.txt") as file:
        cards = file.readlines()
        cards = [line.rstrip('\n') for line in cards]
    deck = [["D " + item for item in cards],
            ["H " + item for item in cards],
            ["C " + item for item in cards],
            ["S " + item for item in cards]
            ]

def first_cards():
    return