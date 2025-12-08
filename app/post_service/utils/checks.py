import grpc 

from app.core.db.repositories.user_repositories import SQLAlchemyUserRepository
from app.core.db.models.user import User

async def check_in_db(
    db:User|None|list[User]|None,
    context,
)->None:
    
    if db is None:
        await context.abort(grpc.StatusCode.NOT_FOUND, "Not found")
    return None