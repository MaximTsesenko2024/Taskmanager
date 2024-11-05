from fastapi import APIRouter


task_router = APIRouter(prefix='/task', tags=['task'])


@task_router.get('/')
async def get_all_tasks():
    pass


@task_router.get('/task_id')
async def get_task_by_id():
    pass


@task_router.post('/create')
async def create_task():
    pass

@task_router.delete('/delete')
async def delete_task():
    pass
