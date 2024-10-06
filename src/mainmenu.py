import time


# Usein toistuvia printtejä
MENU_COMMAND_INSTRUCTIONS = "\nVALITSE KIRJOITTAMALLA VAIHTOEHTOA VASTAAVA NUMERO: "
MENU_COMMAND_FALSE = "ANNETTU KOMENTO EI VASTAA ANNETTUJA VAIHTOEHTOJA"

# Valintojen sanakirjat
MAIN_MENU_CHOICES = {"1": ":ALOITA PELI:", "2": ":HIGHSCORET:", "3": ":CREDITS:", "4": ":SULJE PELI:"}
DIFFICULTIES = {"1": ":HELPPO:", "2": ":NORMAALI:", "3": ":VAIKEA:", "4": ":TAKAISIN:"}


# Printtaa pelin logon
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

# Printtaa mainmenu vaihtoehdot ja ottaa pelaajan komennon
def mainmenu_selection():

    for i in MAIN_MENU_CHOICES:
        print(i, MAIN_MENU_CHOICES[i])
    menu_command = input(MENU_COMMAND_INSTRUCTIONS)
    return menu_command

def is_command_in_menu(command, menu):

    while command not in menu.keys():
        print(MENU_COMMAND_FALSE)
        menu_command_parameter = input(MENU_COMMAND_INSTRUCTIONS)
    return

def command_to_menu_check(command,menu):

    match command:
        case command if command ==
    return

# Tarkistaa pelaajan komennon ja toimii sen mukaisesti
#def menu_command_check(menu_command_parameter):

    # Tarkistaa onko komento sanakirjassa ja pyytää antamaan uuden kommenon niin kauan kunnes se on
#    while menu_command_parameter not in MAIN_MENU_CHOICES.keys():
#            print(MENU_COMMAND_FALSE)
#            menu_command_parameter = input(MENU_COMMAND_INSTRUCTIONS)

    # Tarkistaa mikä annettu komento on ja toimii sen mukaisesti
#    while menu_command_parameter != "4":
#        if menu_command_parameter == "1":
#            for i in DIFFICULTIES:
#                print(DIFFICULTIES[i])
#
#            menu_command_parameter = input(MENU_COMMAND_INSTRUCTIONS)
#
#            if menu_command_parameter == "1":
#                print(f"helppo placeholder")
#            elif menu_command_parameter == "2":
#                print("normaali placeholder")
#            elif menu_command_parameter == "3":
#                print("vaikea placeholder")
#            elif menu_command_parameter == "4":
#                print("takaisin placeholder")
#        elif menu_command_parameter == "2":
#            print("highscore placeholder")
#        elif menu_command_parameter == "3":
#            print("credits placeholder")
#        elif menu_command_parameter == "4":
#            print(f"SULJETAAN PELIÄ...")
#            time.sleep(1)
#            exit()

#    return

if __name__ == "__main__":
    print_logo()

#    menu_command_check(mainmenu_selection())
