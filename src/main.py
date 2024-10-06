import databases as db
import accountlogic
import mainmenu
from src.accountlogic import create_account
from src.mainmenu import print_logo, menu_selection, command_to_main_menu_check, command_to_difficulty


def main() -> None:

    print("1")

    select = input("Syötä 1 jos haluat luoda käyttäjän, 2 jos haluat kirjautua sisään. ")

    if select == "1":
        create_account()
    elif select == "2":
        print("Tule sisään : ")
        #login()
    else:
        print("Väärin meni :(")

    print_logo()
    menu_selection()
    command_to_main_menu_check()
    command_to_difficulty()


if __name__ == '__main__':
    main()
