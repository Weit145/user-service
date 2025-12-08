from abc import ABC, abstractmethod
from proto import user_post_pb2

class IPostServiceImpl(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    async def GetByUsername(self, request,context)->user_post_pb2.UserId:
        pass

    @abstractmethod
    async def GetByID(self, request,context)->user_post_pb2.UserUsername:
        pass