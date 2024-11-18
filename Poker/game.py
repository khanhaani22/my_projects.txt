
def createdeck():
    global deck
    global cards
    with open(Poker/deck.txt) as file:
        cards = file.read() 
    deck =[[],[],[],[]]
    print (cards)
    

createdeck()