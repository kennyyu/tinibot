# alcoholic drinks: [purple: gin, blue: rum, green: vodka, yellow: cranberry, orange: OJ, red: tonic]
# non-alcoholic: [purple: lemonade, blue: apple, green: iced tea, yellow: cranberry, orange: OJ, red: seltzer]

DRINKS = {
# alcoholic drinks
     "gilbert": [0, 0, 2, 1, 0, 1],
     "vodka tonic": [0, 0, 1, 0, 0, 2],
     "screwdriver": [0, 0, 1, 0, 2, 0],
     "gin and tonic": [1, 0, 0, 0, 0, 1],
     "vodka cranberry": [0, 0, 2, 3, 0, 0],
     "cape codder": [0, 0, 0, 2, 3, 0],
     "madras": [0, 0, 2, 4, 1, 0],
     "cranberry gin": [2, 0, 0, 3, 0, 0],
     "orange blossom": [1, 0, 0, 0, 2, 0],
     "rum tonic": [0, 2, 0, 0, 0, 3],
     "rum punch": [0, 2, 0, 1, 4, 0],

# drinks for clearing the bottles
#     "purple": [1,0,0,0,0,0],
#     "blue": [0,1,0,0,0,0],
#     "green": [0,0,1,0,0,0],
#     "yellow": [0,0,0,1,0,0],
#     "orange": [0,0,0,0,1,0],
#     "red": [0,0,0,0,0,1],

# drinks for the fair
#    "rainbow": [1,1,1,1,1,1],
#    "apple seltzer": [1,0,0,0,0,1],
#    "orange seltzer": [0,0,0,0,1,1],
#    "cranberry seltzer": [0,0,0,1,0,1],
#    "arnold palmer": [0,1,1,0,0,0],
#    "pink lemonade": [0,4,0,1,0,0],
#    "citrus spritz": [0,1,0,0,1,2],
#    "cranberry orange": [0,0,0,1,1,0],
#    "cranberry orange":[1,0,0,1,0,0],
#    "rainbow": [1,0,2,1,1,0],
#    "apple lemonade": [1,1,0,0,0,0],
#    "sunrise spritz": [0,0,0,1,1,2]
}

# TODO
# Figure out how much liquid can dispense in a second,
# and adjust the multiplier.
#
# The final times will be in ms.
TIME_MULTIPLIER = 5000

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
