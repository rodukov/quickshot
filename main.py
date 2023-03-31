from PIL import ImageGrab
import pytesseract
import pyautogui
from time import sleep

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR'+'\ '.replace(" ", "")+"tesseract.exe"

def main():
    screenshot = ImageGrab.grab()

    sleep(1.5)

    bbox = (100, 100, 200, 200)
    print(bbox)
    screenshot = ImageGrab.grab(bbox)
    screenshot.save('image.png')

def recognise():
    from PIL import Image

    image = Image.open('image.png')

    text = pytesseract.image_to_string(image)
    print(text)

main()
recognise()