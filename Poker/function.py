import game
def gui_1():
    print("-=+=-=+=-=+=-=+=-")
    print("------POKER------")
    print("-----1.VS AI-----")
    print("-----2.CLOSE-----")
    print("-=+=-=+=-=+=-=+=-")
    
def start():
    gui_1()
    global x
    x = int(input("-Choose number: "))
    if x == 1:
        seq1()
    if x == 2:
        exit()

def game_gui():
    print("-=+=-=+=-=+=-=+=-")
    print("---Dealt Cards---")
    print("--{dealt1}-{dealt2}-{dealt3}---{turn}---{river}--")  
    print("-----------------")
    print("-AI: {}  {} -")
    print("-----------------")
    print("---YOUR  CARDS---")
    print("-{} {}-")
    print("-=+=-=+=-=+=-=+=-")
      

def seq1():
    import random
    createdeck()
    first_cards()
    game_gui()
    print(random.choice(random.choice(deck)))
    
    
start()
