from ..tools.simpleActions import Actions
import time

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
        gold = Actions.read_text_from_region(screenshot=screen, x1=0, y1=183, x2=314, y2=228)
        elixir = Actions.read_text_from_region(screenshot=screen, x1=0, y1=253, x2=314, y2=298)
        gold = Actions.clean_ocr_number(gold)
        elixir = Actions.clean_ocr_number(elixir)
        total = gold + elixir
    
        if total < 600000:
            Actions.tap(2199, 1269) # Next
            time.sleep(1)
        else: 
            print("Base Found. Now start making attack strat")
            break
        
        

def edragRageStrategy():

    # CV map the base with red-border outline

    # deploy edrags
    # deploy heros
    # deploy spells

    # conclude attack, repeat

    return 0

