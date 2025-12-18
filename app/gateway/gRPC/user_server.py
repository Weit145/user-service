from proto import user_pb2_grpc

from app.gateway.services.user_service import UserServiceImpl


class UserServicer(user_pb2_grpc.UserServicer):
    async def DeleteUser(self, request, context):
        return await UserServiceImpl().DeleteUser(request, context)

    async def GetUser(self, request, context):
        return await UserServiceImpl().GetUser(request, context)

    async def UserUpdate(self, request, context):
        return await UserServiceImpl().UserUpdate(request, context)
