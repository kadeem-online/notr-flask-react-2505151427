# third party imports
from flask import Blueprint

# local application imports
from backend.utilities.functions import formatResponse

# Blueprint for API v1 routes
blueprint = Blueprint('api_v1', __name__, url_prefix='/api/v1')


@blueprint.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    Index route for the API v1.
    """

    return formatResponse(
        status=200,
        message="API v1 is running",
    )
