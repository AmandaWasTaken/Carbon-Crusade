# TODO
# lisää random eventtejä ja implementointi pääohjelmaan
from random import randint

def negative_event(score: float) -> (float, int, str):
    turn_modifier = 1
    event = randint(1, 5)
    event_text = ""

    if event == 1:
        event_text = "A new regulation will make flying more difficult and slow down routes. One flight takes 2 months."
        turn_modifier -= 1
    elif event == 2:
        event_text = "The airline has a technical problem. One flight takes 3 months."
        turn_modifier -= 2
    elif event == 3:
        event_text = "The flight was not fully booked. Emissions are reduced by 40%."
        score *= 0.6
    elif event == 4:
        event_text = "The airline is testing a new fuel with 20% lower emissions than the previous one."
        score *= 0.8
    elif event == 5:
        event_text = "A sudden thunderstorm makes flying dangerous. The turn lasts 1.5 months."
        turn_modifier -= 1.5

    return score, turn_modifier, event_text


def positive_event(score: float) -> (float, int, str):
    turn_modifier = 1
    event = randint(1, 5)
    event_text = ""

    if event == 1:
        event_text = "Weather conditions are ideal and your flights take less time. The turn takes only 0.5 months."
        turn_modifier += 0.5
    elif event == 2:
        event_text = "There are delays at the airport and the plane has to circle in the air for an extra hour. You get 30% more emissions."
        score *= 1.3
    elif event == 3:
        event_text = "Air traffic is calm, which shortens flight paths. The turnaround time is only 0.75 months."
        turn_modifier = 0.75
    elif event == 4:
        event_text = "There is a problem with the aircraft engine. You get 20% more emissions."
        score *= 1.2
    elif event == 5:
        event_text = "Your plane is almost completely booed by an american tourism company. The flight's emissions are 50% higher"
        score *= 1.5

    return score, turn_modifier, event_text


def create_random_event(option: str, score: float, turn_modifier: float) -> (float, float, str):
    if option == "Positive":
        score, turn_modifier, event_text = positive_event(score)
    elif option == "Negative":
        score, turn_modifier, event_text = negative_event(score)
    return score, turn_modifier, event_text

