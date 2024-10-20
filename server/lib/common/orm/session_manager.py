# from typing import Type, TypeVar, Generic, List, Optional, Callable, Awaitable, Any
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.future import select
# from sqlalchemy.exc import SQLAlchemyError
# from . import db
# import functools

# def session_manager(func: Callable[[AsyncSession, Any], Awaitable]) -> Callable[[Any], Awaitable]:
#     """
#     Decorator to manage session creation and lifecycle.
#     """
#     @functools.wraps(func)
#     async def wrapper(self: 'BaseRepository[T]', *args: Any, **kwargs: Any) -> Any:
#         async with db.get_session_factory().create_session() as session:
#             try:
#                 # Begin the transaction automatically using the session context manager
#                 result = await func(self, session, *args, **kwargs)
#                 await session.commit()  # Commit if successful
#                 return result

#             except SQLAlchemyError as e:
#                 await session.rollback()  # Rollback on error
#                 raise e  # Re-raise the exception

#     return wrapper

# async def execute_db(session: AsyncSession, func: Callable[[AsyncSession, Any], Awaitable]):
#     async with session.begin():  # This starts a new transaction
#         await func()
        
# @session_manager
# def do_operation_db():
#     execute_db(User.add())
#     Refresh(User)
    
#     execute_db()