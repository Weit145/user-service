from proto import auth_pb2

from app.core.db.models.user import User

def converter_user_out_response(
    user:User,
)->auth_pb2.UserOutResponse:
    return auth_pb2.UserOutResponse(
        username=user.username,
    )

def convert_update_user(
    request:auth_pb2.UserUpdateRequest,
    user:User,
)->User:
    user.username = request.username
    return user