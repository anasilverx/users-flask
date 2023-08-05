from flask import Blueprint
from flask_login import login_required

message_bp = Blueprint('message', __name__)


@message_bp.route("/inbox")
@login_required
def inbox():
    # Your inbox logic here
    return "Inbox page"