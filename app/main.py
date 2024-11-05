from fastapi import FastAPI
from routers.user import user_router
from routers.task import task_router


api = FastAPI()


@api.get('/')
async def welcome():
    return {"message": "Welcome to Taskmanager"}

api.include_router(user_router)
api.include_router(task_router)
