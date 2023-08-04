from flask import Blueprint

message_bp = Blueprint('message', __name__)

@message_bp.route("/inbox")
def inbox():
    # Your inbox logic here
    return "Inbox page"