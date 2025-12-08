import grpc
from proto import user_post_pb2, user_post_pb2_grpc


from app.post_service.gRPC.post_server import PostServicer

async def serve():
    server = grpc.aio.server()
    user_post_pb2_grpc.add_UserPostServicer_to_server(PostServicer(), server)
    server.add_insecure_port('[::]:50055')
    print("gRPC сервер запущен на порту 50055...")
    await server.start()
    await server.wait_for_termination()
