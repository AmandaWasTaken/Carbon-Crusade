import time

#Printtaa pelin logon
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

def mainmenu_selection():
    choices = {"1": ":ALOITA PELI:", "2": ":VAIKEUSTASO:", "3": ":HIGHSCORET:", "4": ":CREDITS:", "5": ":SULJE PELI:"}
    menu_answer_instructions = "\nVALITSE KIRJOITTAMALLA VAIHTOEHTOA VASTAAVA NUMERO: "

    print(f"\n1 {choices["1"]}\n2 {choices["2"]}\n3 {choices["3"]}\n4 {choices["4"]}\n5 {choices["5"]}")
    menu_answer = input(menu_answer_instructions)
    return menu_answer, choices

def menu_answer_check(menu_answer_parameter,choices_parameter):

    menu_answer_instructions = "\nVALITSE KIRJOITTAMALLA VAIHTOEHTOA VASTAAVA NUMERO: "

    while menu_answer_parameter not in choices_parameter.keys():
            print("ANNETTU KOMENTO EI VASTAA ANNETTUJA VAIHTOEHTOJA")
            menu_answer_parameter = input(menu_answer_instructions)

    return

#difficulties = {1: ":HELPPO:", 2: ":NORMAALI:", 3: ":VAIKEA:", 4: ":TAKAISIN:"}

#if menu_answer == "1":
#    print("starting game placeholder")
#elif menu_answer == "2":
#    print(f":VAIKEUSTASOT:\n1{difficulties[1]}\n2 {difficulties[2]}\n3 {difficulties[3]}\n4 {difficulties[4]}")
#elif menu_answer == "3":
#    print("highscore placeholder")
#elif menu_answer == "4":
#    print("credits placeholder")
#elif menu_answer == "5":
#    print(f"SULJETAAN PELIÄ...")
#    time.sleep(1)
#    exit()

print_logo()
menu_answer_variable, choices_variable = mainmenu_selection()
menu_answer_check(menu_answer_variable,choices_variable)