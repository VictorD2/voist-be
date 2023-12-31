# from flask_jwt_extended import jwt_required, get_jwt_identity
from decora.validator import request_validator
from flask import Blueprint, request, jsonify
from chat.services import create_chat, create_resume
from chat.schemas import CreateChat, CreateResume

chat_bp = Blueprint("chat", __name__, url_prefix="/api/v0/chat")


# CREATE CHAT
@chat_bp.route("", methods=["POST"])
# @jwt_required(locations="headers")
@request_validator(request, CreateChat)
def create():
    # Jwt User

    # Generating a new answer and question
    answer = create_chat(request.json)
    print(answer)
    # Response
    return (
        jsonify({"answer": answer}),
        200,
    )


@chat_bp.route("/resume", methods=["POST"])
# @jwt_required(locations="headers")
@request_validator(request, CreateResume)
def resume():
    # Generating a new answer and question
    answer = create_resume(request.json)
    print(answer)
    return (
        jsonify({"answer": answer}),
        200,
    )
