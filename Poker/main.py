def gui_1():
    print("-=+=--=+=--=+=-")
    print("-----POKER-----")
    print("----1.VS AI----")
    print("----2.CLOSE----")
    print("-=+=--=+=--=+=-")
    
def start():
    gui_1()
    x = input("-Choose number: ")
    if x == 1:
        play()
    if x == 2:
        exit()

