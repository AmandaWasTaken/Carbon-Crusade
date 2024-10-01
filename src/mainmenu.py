import time
def print_logo():
    print(""" ____           _                      
/ ___|__ _ _ __| |__   ___  _ __       
| |   / _` | '__| '_ \\ / _ \\| '_ \\      
| |__| (_| | |  | |_) | (_) | | | |     
\\____\\__,_|_|  |_.__/ \\___/|_| |_|     
/ ___|_ __ _   _ ___  __ _  __| | ___  
| |   | '__| | | / __|/ _` |/ _` |/ _ \\ 
| |___| |  | |_| \\__ \\ (_| | (_| |  __/ 
 \\____|_|   \\__,_|___/\\__,_|\\__,_|\\___|""")
    return

def mainmenu_selections():
    print("\n:ALOITA PELI:\n:VAIKEUSTASO:\n:HIGHSCORET:\n:CREDITS:\n:SULJE PELI:")
    menu_answer = input("KIRJOITA YKSI ANNETUISTA VALINNOISTA: ").lower()
    return menu_answer

def menu_answer_check(menu_answer):
    while menu_answer != "aloita peli" or menu_answer != "vaikeustaso" or menu_answer != "highscoret" or menu_answer != "credits" or menu_answer != "sulje peli":
        if menu_answer == "aloita peli":
            print("starting game placeholder")
        elif menu_answer == "vaikeustaso":
            print(":VAIKEUSTASOT:\n:HELPPO:\n:NORMAALI:\n:VAIKEA:\n:TAKAISIN:")
            menu_answer = input("KIRJOITA YKSI ANNETUISTA VAIHTOEHDOISTA: ").lower()
            if menu_answer == "takaisin":
                mainmenu_selections()
        elif menu_answer == "highscoret":
            print("highscore placeholder")
        elif menu_answer == "credits":
            print("credits placeholder")
        elif menu_answer == "sulje peli":
            print(f"SULJETAAN PELIÄ...")
            time.sleep(2)
            exit()
        else:
            print("ANNETTU KOMENTO EI VASTAA ANNETTUJA VAIHTOEHTOJA")
            menu_answer = input("KIRJOITA YKSI ANNETUISTA VALINNOISTA: ").lower()

    return

print_logo()
menu_answer_check(mainmenu_selections())