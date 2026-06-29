import os
import subprocess
import time
import numpy as np
import cv2
import datetime
import pytesseract
from PIL import Image

# Tab S8
DEVICE_ID = "R52T501DACZ"
PROJECT_FOLDER = "/home/braedon/Projects/clashbot/screenshots"
ICONS_FOLDER = "/home/braedon/Projects/clashbot/icons"

# Samsung S23 - 1080x2340
length = 2340
width = 1080

class Actions:
    def tap(x, y):
        subprocess.run(
            ["adb", "-s", DEVICE_ID, "shell", "input", "tap", str(x), str(y)]
        )
        time.sleep(0.7)


    def swipe(x1, y1, x2, y2, duration_ms=600):
        subprocess.run([
            "adb", "-s", DEVICE_ID,
            "shell", "input", "swipe",
            str(x1), str(y1), str(x2), str(y2),
            str(duration_ms)
        ])
        time.sleep(0.9)


    def drag(x1, y1, x2, y2, duration_ms=1000):
        """
        not implemented yet
        """
        return 0


    def screenshot():
        """
        screen = Actions.screenshot()
        """
        result = subprocess.run(
            ["adb", "-s", DEVICE_ID, "exec-out", "screencap", "-p"],
            capture_output=True
        )
        img_array = np.frombuffer(result.stdout, dtype=np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        return img


    def save_screenshot(filename=None, save_path=None, image=None):
        """
        Takes a new screenshot, then saves it. You can also take an image, then save
        by utilizing the 'image' arg. 

        If filename is none, filename = datetime. 
        
        save_path=None Saves to clashbot/screenshots/
        """
        if filename is None:
            filename = f"screen_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        
        if save_path: save_path = save_path
        else: save_path = os.path.join(PROJECT_FOLDER, filename)
        print(save_path)

        if image is None:
            result = subprocess.run(
                ["adb", "-s", DEVICE_ID, "exec-out", "screencap", "-p"],
                capture_output=True
            )
        else: result = image

        with open(save_path, "wb") as f:
            f.write(result.stdout)
        
        print(f"Screenshot saved to {save_path}")
        return save_path


    def findIcon(screenshot, template_path, threshold=0.8, returnCords=False):
        """
        Finds the input icon and taps it. returnCords provides the x and y cords and
        doesn't tap. 
        """
        # load both images
        screen = screenshot
        template_path = os.path.join(ICONS_FOLDER, template_path)
        template = cv2.imread(template_path)
    
        # run template matching
        result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        
        # find the best match location
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        
        if max_val >= threshold:
            # max_loc is top left corner of match, adjust to center
            h, w = template.shape[:2]
            center_x = max_loc[0] + w // 2
            center_y = max_loc[1] + h // 2
            
            print(f"Found at ({center_x}, {center_y}) with confidence {max_val:.2f}")
            if returnCords == False:
                Actions.tap(center_x, center_y)
            else: 
                return center_x, center_y
        else:
            print(f"Not found, best confidence was {max_val:.2f}")

        return None
    

    def read_text_from_region(screenshot, x1, y1, x2, y2):
        """
        returns text strip
        """
        # crop to just the region with the number
        region = screenshot[y1:y2, x1:x2]
        
        # convert to PIL format for tesseract
        pil_image = Image.fromarray(cv2.cvtColor(region, cv2.COLOR_BGR2RGB))
        
        text = pytesseract.image_to_string(pil_image, config='--psm 7 digits')
        return text.strip()
        

    