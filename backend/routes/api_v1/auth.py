"""
Contains the authentication reoutes for teh API.
"""

# third party imports
from flask import Blueprint, current_app, request
from sqlalchemy import select
from werkzeug.security import generate_password_hash

# local application imports
from backend.extensions import database
from backend.models import User
from backend.utilities.functions import formatResponse

# create auth blueprint
blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@blueprint.route('/register', methods=['POST'], strict_slashes=False)
def register():
    """
    Route for user registration.
    """
    # get data from request
    data = request.get_json()

    email = data.get('email', None)
    password = data.get('password', None)
    confirm_password = data.get('confirm_password', None)

    # GUARD: check if email, password and confirm_password are provided
    if not email or not password or not confirm_password:
        missing_field = "email" if not email else "password" if not password else "confirm_password"

        return formatResponse(
            status=400,
            message="Email, password, and confirm password are requred.",
            errors=[f"Missing field: {missing_field}"]
        )

    # GUARD: check if password length is less than 8 characters
    MIN_PASSWORD_LENGTH = 8
    if len(password) < MIN_PASSWORD_LENGTH:
        return formatResponse(
            status=400,
            message="Password is too short.",
            errors=[
                f"Password must be at least {MIN_PASSWORD_LENGTH} characters long."],
        )

    # GUARD: check if password and confirm_password match
    if password != confirm_password:
        return formatResponse(
            status=400,
            message="Passwords do not match.",
            errors=['Password does not match confirm password.']
        )

    # GUARD: check email format
    # TODO: implement email format validation

    # GUARD: check if email is already registered.
    with current_app.app_context():
        stmt = select(User).where(User.email == email)
        existing_user = database.session.execute(stmt).scalar_one_or_none()

        if existing_user:
            return formatResponse(
                status=400,
                message="Email already registered.",
                errors=["The email address is already in use."]
            )

    try:
        # hash the password
        hashed_password = generate_password_hash(str(password))

        # create new user
        new_user = User(
            email=email,
            password=hashed_password
        )

        with current_app.app_context():
            database.session.add(new_user)
            database.session.commit()

        return formatResponse(
            status=201,
            message="User created successfully.",
        )

    except Exception as e:
        return formatResponse(
            status=500,
            message="An error occured when creating the user!",
            errors=[str(2)]
        )
