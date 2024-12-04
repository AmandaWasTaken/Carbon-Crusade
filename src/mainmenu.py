import time
import gameplay
import top5highscore
#import highscoreasettaminen
from src.gameplay import startGameplayLoop

# Usein toistuvia printtejä
MENU_COMMAND_INSTRUCTIONS = "\nVALITSE KIRJOITTAMALLA VAIHTOEHTOA VASTAAVA NUMERO: "
MENU_COMMAND_FALSE = "ANNETTU KOMENTO EI VASTAA ANNETTUJA VAIHTOEHTOJA"

# Käytettävät dictionaryt ja tuplet
MAIN_MENU_CHOICES = {"1": ":ALOITA PELI:", "2": ":HIGHSCORET:", "3": ":CREDITS:", "4": ":SULJE PELI:"}
DIFFICULTIES = {"1": ":HELPPO:", "2": ":NORMAALI:", "3": ":VAIKEA:", "4": ":TAKAISIN:"}
CREDITS = ("JUHO MOLIN", "TEPPO TOROPAINEN", "ATTE STEN", "AMANDA SANDELL", "JERE PUNNONEN")

# Printtaa pelin logon
def print_logo():
    print(""" ____            _                      
/ ___|__ _ _ __ | |__   ___  _ __       
| |   / _` | '__| '_ \\ / _ \\| '_ \\      
| |__| (_| | |  | |_) | (_) | | | |     
\\____\\__,_ |_|  |_.__/ \\___/|_| |_|     
/ ___|_ __ _   _ ___  __ _   __| | ___  
| |   | '__| | | / __|/ _` |/ _` |/ _ \\ 
| |___| |  | |_| \\__ \\ (_| | (_| |  __/ 
 \\____|_|   \\__,_|___/\\__,_|\\__,_|\\___|""")
    return

# Printtaa mainmenu vaihtoehdot ja ottaa pelaajan komennon
def menu_selection(choices,user):

    print()
    for i in choices:
        print(i, choices[i])
    menu_command = input(MENU_COMMAND_INSTRUCTIONS)
    return menu_command

# Testaa onko komento validi
def is_command_in_menu(command,menu,user):

    while command not in menu.keys():
        print(MENU_COMMAND_FALSE)
        command = input(MENU_COMMAND_INSTRUCTIONS)
    return

# Suorittaa main menu vaihtoehdoilla menu_selection(), sitten tarkistaa tuloksen ja toimii sen mukaisesti
def command_to_main_menu_check(command, user):

    is_command_in_menu(command, MAIN_MENU_CHOICES,user)

    if command == "1":
        command_to_difficulty(command,user)
    elif command == "2":
        top5highscore.get_top_scores()
        command_to_main_menu_check(menu_selection(MAIN_MENU_CHOICES,user),user)
    elif command == "3":
        print("CREDITS\n")
        for i in CREDITS:
            print(f":{i}:")
        command_to_main_menu_check(menu_selection(MAIN_MENU_CHOICES,user),user)
    elif command == "4":
        print("suljeetaan peliä...")
        time.sleep(1)
        exit()

    return

# Suorittaa vaikeustaso vaihtoehdoilla menu_selection(), sitten tarkistaa tuloksen ja toimii sen mukaisesti
def command_to_difficulty(command,user):

    command = menu_selection(DIFFICULTIES,user)
    is_command_in_menu(command, DIFFICULTIES,user)

    if command == "1":
        score = startGameplayLoop(1)
    elif command == "2":
        score = startGameplayLoop(2)
    elif command == "3":
        score = startGameplayLoop(3)
    elif command == "4":
        print_logo()

    command_to_main_menu_check(menu_selection(MAIN_MENU_CHOICES,user),user)

    return

# Suorittaa koko main menu koodin
def run_main_menu(user):
    print_logo()
    command_to_main_menu_check(menu_selection(MAIN_MENU_CHOICES,user),user)

# if __name__ == "__main__":
#     print_logo()
#     command_to_main_menu_check(menu_selection(MAIN_MENU_CHOICES))
