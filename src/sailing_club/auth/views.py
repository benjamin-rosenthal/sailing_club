from flask import jsonify, request, render_template, Blueprint
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from sqlmodel import Session, select
from sailing_club.app import db
from sailing_club.auth.models.user import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

# from sqlalchemy import text
from sailing_club.app import engine

# @app.route("/")
# def hello_world():
    
#     with engine.connect() as conn:
#      result = conn.execute(text("select 'hello world'"))
#      return("success")

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@bp.route("/login", methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        with Session(engine) as session:
            loggingInUser = session.exec(select(User).where(User.username == request.json.get("username", None)))
            if loggingInUser == None:
                return jsonify({"msg": "Bad username or password"}), 401

            access_token = create_access_token(identity=loggingInUser.username)
            return jsonify(access_token=access_token)
    
    return render_template('auth/login.html')


# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

# # Test endpoint to get all users
# @app.route("/users", methods=["GET"])
# def getUsers():
#     session = Session(engine)
#     stmt = select(User)
#     for user in session.scalar(stmt):
#         print(user)
#     return ""

# @app.route("/user", methods=["POST"])
# def addUser():
#     with Session(engine) as session:
#         spongebob = User(
#             email='test',
#             password='test'
#         )

#         session.add_all([spongebob])

#         session.commit()