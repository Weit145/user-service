from abc import ABC, abstractmethod

from ..models.user import User

class IUserRepository(ABC):

    @abstractmethod
    async def create_user(self, user: User) -> None:
        pass

    @abstractmethod
    async def get_user_by_id_auth(self, id_auth: int) -> User | None:
        pass
    
    @abstractmethod
    async def delete_user(self, user: User,context) -> None:
        pass

    @abstractmethod
    async def update_user(self, user: User,context) -> None:
        pass