from proto import user_pb2

from app.core.db.models.user import User

def converter_user_out_response(
    user:User,
)->user_pb2.UserOutResponse:
    return user_pb2.UserOutResponse(
        username=user.username,
    )

def convert_update_user(
    request:user_pb2.UserUpdateRequest,
    user:User,
)->User:
    user.username = request.username
    return user