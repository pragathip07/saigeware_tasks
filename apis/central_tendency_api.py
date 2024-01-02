from flask import request, Blueprint
from flask_cors import CORS
import numpy as np
from config import logger


compute_central_tendency_api = Blueprint('endpoint2', __name__)
CORS(compute_central_tendency_api)


@compute_central_tendency_api.route('/task1/endpoint2', methods=['POST'])
def compute_central_tendency():

    json_object = request.get_json()
    numbers = json_object['numbers']
    logger.info("Received the list of numbers : {}".format(' '.join(map(str, numbers))))
    numbers = np.array(numbers).astype(float)

    measures = {'Mean': np.mean(numbers), 'Median': np.median(numbers), 'Standard Deviation': np.std(numbers),
                '25th percentile': np.percentile(numbers, 25), '75th percentile': np.percentile(numbers, 75),
                'Minimum': np.min(numbers), 'Maximum': np.max(numbers)}

    return measures
