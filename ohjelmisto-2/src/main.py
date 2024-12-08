import databases as db
import accountlogic as al
import mainmenu


def main() -> None:

    user = al.Account()
    username = None
    while True:
        select = input("Syötä 1 jos haluat luoda käyttäjän, 2 jos haluat kirjautua sisään. ")
        if select == "1":
            username = user.create_account()
            break
        elif select == "2":
            username = user.login()
            break
        else:
            print("Virheellinen syöte, yritä uudestaan.")

    mainmenu.mainmenu()


if __name__ == '__main__':
    main()
