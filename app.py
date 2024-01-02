import os

from flask import Flask
import argparse


from apis.health_check_api import get_app_health_api
from apis.text_extraction_from_image_api import extract_text_from_image_api
from apis.central_tendency_api import compute_central_tendency_api


app = Flask(__name__)


app.register_blueprint(get_app_health_api)
app.register_blueprint(extract_text_from_image_api)
app.register_blueprint(compute_central_tendency_api)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    sys_args = parser.parse_args()
    app.run(host="0.0.0.0", port=8080)
