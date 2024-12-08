def print_logo():
    print(""" ____           _                      
/ ___|__ _ _ __| |__   ___  _ __       
| |   / _` | '__| '_ \ / _ \| '_ \      
| |__| (_| | |  | |_) | (_) | | | |     
\____\__,_|_|  |_.__/ \___/|_| |_|     
/ ___|_ __ _   _ ___  __ _  __| | ___  
| |   | '__| | | / __|/ _` |/ _` |/ _ \ 
| |___| |  | |_| \__ \ (_| | (_| |  __/ 
 \____|_|   \__,_|___/\__,_|\__,_|\___|""")
    return

def print_menu_selections():
    print("\n:ALOITA PELI:\n:VAIKEUSTASO:\n:HIGHSCORET:\n:CREDITS:\n:SULJE PELI:")
    return


def mainmenu():

    print_logo()
    print_menu_selections()
    menu_answer = input("KIRJOITA YKSI ANNETUISTA VALINNOISTA: ").lower()
    while True: 
        if menu_answer == "aloita peli":
            print("starting game placeholder")
            break
        elif menu_answer == "vaikeustaso":
            print("difficulty placeholder")
            break
        elif menu_answer == "highscoret":
            print("highscore placeholder")
            break
        elif menu_answer == "credits":
            print("credits placeholder")
            break
        elif menu_answer == "sulje peli":
            print("closing game placeholder")
            break
        else:
            print("ANNETTU KOMENTO EI VASTAA ANNETTUJA VAIHTOEHTOJA")
            menu_answer = input("KIRJOITA YKSI ANNETUISTA VALINNOISTA: ")
            menu_answer = menu_answer.lower()

if __name__ == '__main__':
    mainmenu()
