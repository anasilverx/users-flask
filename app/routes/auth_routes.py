from flask import Blueprint, request, jsonify
from flask_login import login_required, logout_user
from flask_cors import CORS, cross_origin
from flask_bcrypt import Bcrypt 
from app.models.user import User
from app import db

auth_bp = Blueprint('auth', __name__)

bcrypt = Bcrypt()

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

    # login_user()

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

    # login_user()
    return jsonify({
        "id": user.id,
        "email": user.email
    })

# @auth_bp.route("/logout", methods=["POST"])
# @login_required
# def logout():
#     logout_user()
#     flash("You were logged out.", "success")
#     return redirect(url_for("accounts.login"))