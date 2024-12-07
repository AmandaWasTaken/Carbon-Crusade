# TODO
# lisää random eventtejä ja implementointi pääohjelmaan
from random import randint

def negative_event(score: float) -> (float, int):
    turn_modifier = 1
    event = randint(1, 5)

    if event == 1:
        print("uusi sääntely vaikeuttaa lentämistä, mikä hidastaa reittejä. Yksi vuoro kestää 2 kuukautta.")
        turn_modifier = 2
    elif event == 2:
        print("lentokoneyhtiöllä on tekninen ongelma. Yksi vuoro vie 3 kuukautta.")
        turn_modifier = 3
    elif event == 3:
        print("yllättävä lakko pakottaa sinut perumaan lentoja. Lentopäästöt vähenevät 40%.")
        score *= 0.6
    elif event == 4:
        print("lentoyhtiölläsi on testissä uusi polttoaine, jonka päästöt ovat 20% pienemmät kuin aiemman")
        score *= 0.8
    elif event == 5:
        print("ukkosmyrsky tekee lentämisestä vaarallista. Vuoro kestää 1.5 kuukautta.")
        turn_modifier = 1.5

    return score, turn_modifier


def positive_event(score: float) -> (float, int):
    turn_modifier = 1
    event = randint(1, 5)

    if event == 1:
        print("sääolosuhteet ovat ihanteelliset, ja lentosi kestävät vähemmän aikaa. Vuoro kestää vain 0.5 kuukautta.")
        turn_modifier = 0.5
    elif event == 2:
        print("lentokentällä on myöhästymisiä ja lentokone joutuu kiertämään ilmassa ylimääräisen tunnin. Saat 30% enemmän päästöjä.")
        score *= 1.3
    elif event == 3:
        print("ilmaliikenne on rauhallista, mikä lyhentää lentoreittejä. Vuoro kestää vain 0.75 kuukautta.")
        turn_modifier = 0.75
    elif event == 4:
        print("lentokentän yhteistyösopimus tarjoaa erikoisedut. Saat 20% enemmän päästöjä.")
        score *= 1.2
    elif event == 5:
        print("lentokoneesi on lähes täysin buukattu amerikkalaisen matkailuyrityksen toimesta. lennon päästöt ovat 50% korkeammat")
        score *= 1.5

    return score, turn_modifier


def create_random_event(option: str, score: float, turn_modifier: float) -> (float, float):
    if option == "Positive":
        score, turn_modifier = positive_event(score)
    elif option == "Negative":
        score, turn_modifier = negative_event(score)
    else:
        print(f"Invalid option {option}! ")
        exit(-1)
    return score, turn_modifier

