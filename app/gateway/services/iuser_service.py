from abc import ABC, abstractmethod
from proto import user_pb2

class IUserServiceImpl(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    async def DeleteUser(self, request,context)->user_pb2.Empty:
        pass

    @abstractmethod
    async def GetUser(self, request,context)->user_pb2.UserOutResponse:
        pass

    @abstractmethod
    async def UserUpdate(self, request,context)->user_pb2.UserOutResponse:
        pass