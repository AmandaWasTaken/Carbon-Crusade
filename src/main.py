import databases as db
import accountlogic
import mainmenu
from src.accountlogic import create_account, login
from src.mainmenu import run_main_menu


def main() -> None:
    while True:
        select = input("Syötä 1 jos haluat luoda käyttäjän, 2 jos haluat kirjautua sisään. ")
        if select == "1":
            create_account()
            break
        elif select == "2":
            # login()
            break
        else:
            print("Virheellinen syöte, yritä uudestaan.")

    run_main_menu()


if __name__ == '__main__':
    main()
