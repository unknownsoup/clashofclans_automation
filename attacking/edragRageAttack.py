from ..upgrading.simpleActions import Actions

# Galaxy Tab S8 - 2560x1600
length = 2560
width = 1600

def attack_sequence():
    # begin init attacking
    # Home Base Attack Button - Big Square
    Actions.tap(x = length * 0.0909, y = width * 0.9)
    # Battle Button, to start a raid
    Actions.tap(x = length * 0.1364, y = width * 0.7)
    # Army confirmation screen
    Actions.tap(x=2199, y=1304)
    
    # combine gold and elixir values to attack if 600k+
    # if not, skip
    
    # CV map the base with red-border outline

    # deploy edrags
    # deploy heros
    # deploy spells

    # conclude attack, repeat

    return 0



attack_sequence()
