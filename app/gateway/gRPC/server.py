import grpc
from proto import user_pb2_grpc, user_pb2

from app.gateway.gRPC.user_server import UserServicer

async def serve():
    server = grpc.aio.server()
    user_pb2_grpc.add_UserServicer_to_server(UserServicer(), server)
    server.add_insecure_port('[::]:50052')
    print("gRPC сервер запущен на порту 50052...")
    await server.start()
    await server.wait_for_termination()
