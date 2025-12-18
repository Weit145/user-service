from sqlalchemy import select

from ..db_hellper import db_helper
from ..models.user import User
from .iuser_repositories import IUserRepository


class SQLAlchemyUserRepository(IUserRepository):
    async def create_user(self, user: User) -> None:
        try:
            async with db_helper.transaction() as session:
                session.add(user)
        except Exception:
            raise

    async def get_user_by_id_auth(self, id_auth: int) -> User | None:
        async with db_helper.transaction() as session:
            result = await session.execute(select(User).where(User.id_auth == id_auth))
            return result.scalar_one_or_none()

    async def get_user_by_username(self, username: str) -> User | None:
        async with db_helper.transaction() as session:
            result = await session.execute(
                select(User).where(User.username == username)
            )
            return result.scalar_one_or_none()

    async def get_users_by_ids_auth(self, ids_auth: list[int]) -> list[User]:
        if not ids_auth:
            return []
        async with db_helper.transaction() as session:
            result = await session.execute(
                select(User).where(User.id_auth.in_(ids_auth))
            )
            return result.scalars().all()

    async def delete_user(self, user: User, context) -> None:
        async with db_helper.transaction() as session:
            await session.delete(user)

    async def update_user(self, user: User, context) -> None:
        async with db_helper.transaction() as session:
            session.add(user)
