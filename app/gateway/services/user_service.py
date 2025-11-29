from app.core.db.models.user import User
from proto import user_pb2_grpc, user_pb2

from app.core.db.repositories.user_repositories import SQLAlchemyUserRepository
from app.gateway.services.iuser_service import IUserServiceImpl
from app.kafka.repositories.kafka_repositories import KafkaRepository

from app.gateway.utils.checks import (
    check_in_db,
)
from app.gateway.utils.convert import (
    converter_user_out_response,
    convert_update_user,
)


class UserServiceImpl(IUserServiceImpl):
    def __init__(self):
        self.repo = SQLAlchemyUserRepository()
        self.kf = KafkaRepository()


    async def DeleteUser(self, request,context)->user_pb2.Empty:
        user = await self.repo.get_user_by_id(request.id,context)
        await check_in_db(user,context)

        await self.repo.delete_user(request.id,context)
        return user_pb2.Empty()

    async def GetUser(self, request,context)->user_pb2.UserOutResponse:
        user = await self.repo.get_user_by_id(request.id,context)
        await check_in_db(user,context)

        return converter_user_out_response(user)


    async def UserUpdate(self, request,context)->user_pb2.UserOutResponse:
        user = await self.repo.get_user_by_id(request.id,context)
        await check_in_db(user,context)

        result = convert_update_user(request,user)
        await self.repo.update_user(result,context)
        return converter_user_out_response(result)
    
    async def CreateUserFromAuth(self, data:dict) -> None:
        id_auth = data.get("id")
        print(f"Creating user for auth ID: {id_auth}", flush=True)
        username = data.get("username")
        print(f"Username from auth service: {username}", flush=True)
        user = await self.repo.get_user_by_id_auth(id_auth)
        if user is None:
            user_new = User(
                username=username,
                id_auth=id_auth
            )
            await self.repo.create_user(user_new)