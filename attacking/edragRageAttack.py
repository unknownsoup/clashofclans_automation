from ..tools.simpleActions import Actions


# Galaxy Tab S8 - 2560x1600
length = 2560
width = 1600

def begin_attack_sequence():
    """
    Start in homebase. Starts attacking and gets you into the Next, End Battle screen
    """
    # begin init attacking
    # Home Base Attack Button - Big Square
    Actions.tap(x=232, y=1440)
    # Battle Button, to start a raid
    Actions.tap(x=349, y=1120)
    # Army confirmation screen
    Actions.tap(x=2199, y=1304)
    
def find_base():
    """
    Keeps pressing 'Next' until find base with enough loot
    """
    while True:
        screen = Actions.screenshot()
        
        # combine gold and elixir values to attack if 600k+

        # if not, skip
        total = 0
        if total < 600000:
            Actions.tap(2199, 1269)
        else: break
        
        

def edragRageStrategy():

    # CV map the base with red-border outline

    # deploy edrags
    # deploy heros
    # deploy spells

    # conclude attack, repeat

    return 0

