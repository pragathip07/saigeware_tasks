from flask import Blueprint, jsonify
from flask_cors import CORS
from config import logger


get_app_health_api = Blueprint('health', __name__)
CORS(get_app_health_api)


@get_app_health_api.route("/task1/health", methods=['GET'])
def health():
    logger.info("HealthCheck API")
    return jsonify({"status": "up"})

