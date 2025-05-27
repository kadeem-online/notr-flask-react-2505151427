# third party imports
from flask import Blueprint

# local application imports
import backend.routes.api_v1.auth as auth_routes
from backend.utilities.functions import formatResponse

# Blueprint for API v1 routes
blueprint = Blueprint('api_v1', __name__, url_prefix='/api/v1')

# Register subroutes
blueprint.register_blueprint(auth_routes.blueprint)


@blueprint.route('/', methods=['GET', 'POST'], strict_slashes=False)
def index():
    """
    Index route for the API v1.
    """

    return formatResponse(
        status=200,
        message="API v1 is running",
    )
