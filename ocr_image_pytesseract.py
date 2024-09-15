import re
import pytesseract


def ocr_image(image):
    # get pytesseract path for linux
    pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

    custom_config = r'--oem 1 --psm 11'

    # get image text
    text = pytesseract.image_to_string(image, lang='eng', config=custom_config)
    
    # trim text
    text = text.strip()
    
    # remove extra spaces
    text = ' '.join(text.split())
    
    # remove non-alphanumeric characters
    text = re.sub(r'[^A-Za-z0-9\s]+', '', text)
    
    # split text into words
    text_split = text.split()

    return text_split