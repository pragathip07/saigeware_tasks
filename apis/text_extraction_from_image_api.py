from flask import request, Blueprint
import pytesseract
from PIL import Image
from flask_cors import CORS
from config import logger


# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


extract_text_from_image_api = Blueprint('endpoint1', __name__)
CORS(extract_text_from_image_api)


@extract_text_from_image_api.route('/task1/endpoint1', methods=['POST'])
def extract_text_from_image():

    logger.info("Extract Text API")

    if 'image' in request.files:
        image_file = request.files['image']
        logger.info("Received the Image")
    else:
        return 'File Not Present\nPlease Enter a Valid Image File'

    image = Image.open(image_file)
    text = ""

    try:
        text = pytesseract.image_to_string(image)
        logger.info("Extracting Text From The Input Image Data")
    except Exception as E:
        logger.error("Error while extracting the text from the given image data.\nThe error is : ", E)
    return {'text': text}

