# standard library imports
from typing import List

# third party imports
from flask import jsonify


def formatResponse(status: int, message: str, data: dict = None, errors: List[str] = None):
    """
    Formats the information to be returned into a standardized API format.

    args:
        status (int): HTTP status code for the response.
        message (str): A message describing the response.
        data (dict, optional): The data to be included in the response. Defaults to None.
        errors (List[str], optional): A list of error messages, if any. Defaults to None.
    """
    response = jsonify({
        "status": status,
        "message": message,
        "data": data if data is not None else {},
        "errors": errors if errors is not None else []
    })

    return response, status
