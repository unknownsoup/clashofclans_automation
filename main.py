from clashbot.tools.simpleActions import Actions
import cv2

def main():
    
    screen = Actions.screenshot()
    gold_count = Actions.read_text_from_region(screenshot=screen, x1=0, y1=72, x2=314, y2=118)
    print(gold_count)

    return 0


main()