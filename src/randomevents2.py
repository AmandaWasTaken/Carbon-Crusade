# TODO
# lisää random eventtejä ja implementointi pääohjelmaan
from random import randint


def negative_event(score: float):

    event = randint(1,3)
    if event == 1:
        print("lentoyhtiölläsi on testissä uusi polttoaine, jonka päästöt ovat 20% pienemmät kuin aiemman")
        score *= 0.8
    elif event == 2:
        print("lentokone joutuu tekemään hätälaskun matkan loppupäässä. saat vain 70% päästöistä")
        score *= 0.7
    elif event == 3:
        print("lentokoneessa on uudet tehokkaamat moottorit ja ne aiheuttavat 15% vähemmän päästöjä.")
        score *= 0.85

    return score

def positive_event(score: float) -> float:

    event = randint(1,3)
    '''
    match event:
        case 1:
            print("Lentokone on viallinen ja saat tuplapäästöt ")
            score *= 2
        case 2:
            print("lentokoneesi on lähes täysin buukattu amerikkalaisen matkailuyrityksen toimesta. lennon päästöt ovat 50% korkeammat")
            score += score*1.5
        case 3:
            print("lentokentällä on myöhästymisiä ja lentokone joutuu kiertämään ilmassa ylimääräisen tunnin. lennon päästöt ovat 10% korkeammat")
            score = score*1.1
        case _: 
            pass
'''
    if event == 1:
        print("Lentokone on viallinen ja saat tuplapäästöt ")
        score *= 2
    elif event ==  2:
        print("lentokoneesi on lähes täysin buukattu amerikkalaisen matkailuyrityksen toimesta. lennon päästöt ovat 50% korkeammat")
        score += score*1.5
    elif event == 3:
        print("lentokentällä on myöhästymisiä ja lentokone joutuu kiertämään ilmassa ylimääräisen tunnin. lennon päästöt ovat 10% korkeammat")
        score = score*1.1

    return score

def create_random_event(option: str, score: int):
    if option == "Positive":
        score = positive_event(score)
    elif option == "Negative":
        score = negative_event(score)
    else:
        print(f"Invalid option {option}! ")
        exit(-1)
    return score

