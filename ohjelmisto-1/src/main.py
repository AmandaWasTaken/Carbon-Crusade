import databases as db
import accountlogic as al
import mainmenu


def main() -> None:
    while True:
        select = input("Syötä 1 jos haluat luoda käyttäjän, 2 jos haluat kirjautua sisään. ")
        if select == "1":
            user = al.create_account()
            break
        elif select == "2":
            user = al.login()
            break
        else:
            print("Virheellinen syöte, yritä uudestaan.")

    mainmenu.run_main_menu(user)


if __name__ == '__main__':
    main()
