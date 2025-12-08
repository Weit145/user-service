from app.core.db.models.user import User
from proto import user_post_pb2_grpc, user_post_pb2

from app.core.db.repositories.user_repositories import SQLAlchemyUserRepository
from app.post_service.services.ipost_service import IPostServiceImpl

from app.post_service.utils.checks import (
    check_in_db
)

class PostServiceImpl(IPostServiceImpl):
    def __init__(self):
        self.repo = SQLAlchemyUserRepository()


    async def GetByUsername(self, request,context)-> int:
        user = await self.repo.get_user_by_username(request.username)
        await check_in_db(user,context)
        return user_post_pb2.UserId(id = user.id_auth)

    async def GetByID(self, request,context)-> str:
        user = await self.repo.get_user_by_id_auth(request.id)
        await check_in_db(user,context)
        return user_post_pb2.UserUsername(username = user.username)
    
    async def GetByIDs(self, request, context) -> user_post_pb2.UsersMapResponse:
        users = await self.repo.get_users_by_ids_auth(request.ids)
        await check_in_db(users, context)
        users_map = {user.id_auth: user.username for user in users}
        response = user_post_pb2.UsersMapResponse(users=users_map)
        return response
