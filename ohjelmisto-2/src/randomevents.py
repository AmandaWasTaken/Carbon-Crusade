# TODO
# lisää random eventtejä ja implementointi pääohjelmaan
from random import randint

def negative_event(score: float) -> (float, int, str):
    turn_modifier = 1
    event = randint(1, 5)
    event_text = ""

    if event == 1:
        event_text = "uusi sääntely vaikeuttaa lentämistä, mikä hidastaa reittejä. Yksi vuoro kestää 2 kuukautta."
        turn_modifier -= 1
    elif event == 2:
        event_text = "lentokoneyhtiöllä on tekninen ongelma. Yksi vuoro vie 3 kuukautta."
        turn_modifier -= 2
    elif event == 3:
        event_text = "yllättävä lakko pakottaa sinut perumaan lentoja. Lentopäästöt vähenevät 40%."
        score *= 0.6
    elif event == 4:
        event_text = "lentoyhtiölläsi on testissä uusi polttoaine, jonka päästöt ovat 20% pienemmät kuin aiemman"
        score *= 0.8
    elif event == 5:
        event_text = "ukkosmyrsky tekee lentämisestä vaarallista. Vuoro kestää 1.5 kuukautta."
        turn_modifier -= 1.5

    return score, turn_modifier, event_text


def positive_event(score: float) -> (float, int, str):
    turn_modifier = 1
    event = randint(1, 5)
    event_text = ""

    if event == 1:
        event_text = "sääolosuhteet ovat ihanteelliset, ja lentosi kestävät vähemmän aikaa. Vuoro kestää vain 0.5 kuukautta."
        turn_modifier += 0.5
    elif event == 2:
        event_text = "lentokentällä on myöhästymisiä ja lentokone joutuu kiertämään ilmassa ylimääräisen tunnin. Saat 30% enemmän päästöjä."
        score *= 1.3
    elif event == 3:
        event_text = "ilmaliikenne on rauhallista, mikä lyhentää lentoreittejä. Vuoro kestää vain 0.75 kuukautta."
        turn_modifier = 0.75
    elif event == 4:
        event_text = "lentokoneen moottorissa on vikaa. Saat 20% enemmän päästöjä."
        score *= 1.2
    elif event == 5:
        event_text = "lentokoneesi on lähes täysin buukattu amerikkalaisen matkailuyrityksen toimesta. lennon päästöt ovat 50% korkeammat"
        score *= 1.5

    return score, turn_modifier, event_text


def create_random_event(option: str, score: float, turn_modifier: float) -> (float, float, str):
    if option == "Positive":
        score, turn_modifier, event_text = positive_event(score)
    elif option == "Negative":
        score, turn_modifier, event_text = negative_event(score)
    return score, turn_modifier, event_text

