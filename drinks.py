DRINKS = {
    "gilbert": [0, 0, 2, 1, 0, 1],
    "vodka tonic": [0, 0, 1, 0, 0, 2],
    "screwdriver": [0, 0, 1, 0, 2, 0],
    "gin and tonic": [1, 0, 0, 0, 0, 1],
    "vodka cranberry": [0, 0, 2, 3, 0, 0],
    "cape codder": [0, 0, 2, 3, 0, 0],
    "madras": [0, 0, 2, 4, 1, 0],
    "cranberry gin": [2, 0, 0, 3, 0, 0],
    "orange blossom": [1, 0, 0, 0, 2, 0],
    "rum tonic": [0, 2, 0, 0, 0, 3],
    "rum punch": [0, 2, 0, 1, 4, 0],
    "purple": [1,0,0,0,0,0],
    "blue": [0,1,0,0,0,0],
    "green": [0,0,1,0,0,0],
    "yellow": [0,0,0,1,0,0],
    "orange": [0,0,0,0,1,0],
    "red": [0,0,0,0,0,1],
    "rainbow": [1,1,1,1,1,1],
}

# TODO
# Figure out how much liquid can dispense in a second,
# and adjust the multiplier.
#
# The final times will be in ms.
TIME_MULTIPLIER = 1000

def find_drink(text):
    for drink in DRINKS:
        if text.find(drink) != -1:
            return drink
    return ""

def get_times(drink):
    assert(drink in DRINKS)
    ratios = DRINKS[drink]
    s = sum(ratios)
    normalized = [float(r) / s for r in ratios]
    times = [int(x * TIME_MULTIPLIER) for x in normalized]
    return times
