from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, unset_jwt_cookies 
from app.models.user import User
from app import db

auth_bp = Blueprint('auth', __name__)

bcrypt = Bcrypt()
@auth_bp.route('/token', methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    
    user = User.query.filter_by(email=email).first()

    if not user or not bcrypt.check_password_hash(user.password, password):
        return {"msg": "Wrong email or password"}, 401
        
    access_token = create_access_token(identity=email)
    response = {'access_token':access_token}
        
    
    return response 

@auth_bp.route("/register", methods=["POST"])
def register_user():
    email = request.json["email"]
    password = request.json["password"]

    user_exists = User.query.filter_by(email=email).first() is not None

    if user_exists:
        return jsonify({"error": "User already exists"}), 409

    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    new_user = User(email=email, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "id": new_user.id,
        "email": new_user.email
    })

@auth_bp.route("/login", methods=["POST"])
def login_user():
    email = request.json["email"]
    password = request.json["password"]

    user = User.query.filter_by(email=email).first()

    if user is None:
        return jsonify({"error": "Unauthorized"}), 401 
    
    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error": "Unauthorized"}), 401

    return jsonify({
        "id": user.id,
        "email": user.email
    })

@auth_bp.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg":"logout successful"})
    unset_jwt_cookies(response)
    return response

@auth_bp.route("/profile")
def my_profile():
    response_body= {
        "name": "Morti Web App",
        "about": "Hello! Send Farewell"
    }
    return response_body
