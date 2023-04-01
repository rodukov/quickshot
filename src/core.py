from PIL import ImageGrab
import pytesseract
import pyautogui
from time import sleep

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR'+'\ '.replace(" ", "")+"tesseract.exe"

def get_pos():
    pos = pyautogui.position()
    return (pos.x, pos.y)

def check_pos(bbox):
    bbox = list(bbox)
    if bbox[0] > bbox[2]:
        clipboard = bbox[0]
        bbox[0] = bbox[2]
        bbox[2] = clipboard
    if bbox[1] > bbox[3]:
        clipboard = bbox[1]
        bbox[1] = bbox[3]
        bbox[3] = clipboard
    return tuple(bbox)

def main():
    screenshot = ImageGrab.grab()
    f1 = get_pos()
    print(f'Selected F1: {f1}')
    sleep(1.5)
    f2 = get_pos()
    print(f'Selected F2: {f2}')
    bbox = f1+f2
    screenshot = ImageGrab.grab(check_pos(bbox))
    screenshot.save('image.png')

def recognise():
    from PIL import Image

    image = Image.open('image.png')

    text = pytesseract.image_to_string(image)
    print('================================')
    print('Output:\n')
    print(text)
    print('================================')

import keyboard  # using module keyboard
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
            main()
            recognise()
    except:
        break  # if user pressed a key other than the given key the loop will break
