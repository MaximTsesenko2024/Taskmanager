from fastapi import APIRouter


user_router = APIRouter(prefix='/user', tags=['user'])


@user_router.get('/')
async def get_all_users():
    pass


@user_router.get('/user_id')
async def get_user_by_id():
    pass


@user_router.post('/create')
async def create_user():
    pass

@user_router.delete('/delete')
async def delete_user():
    pass
