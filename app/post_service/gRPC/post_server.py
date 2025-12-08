from proto import user_post_pb2_grpc
from app.post_service.services.post_service import PostServiceImpl


class PostServicer(user_post_pb2_grpc.UserPostServicer):
    async def GetByUsername(self, request, context):
        return await PostServiceImpl().GetByUsername(request, context)

    async def GetByID(self, request, context):
        return await PostServiceImpl().GetByID(request, context)