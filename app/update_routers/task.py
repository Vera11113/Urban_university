from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import insert, delete, select, update
from sqlalchemy.orm import Session
from models.task import Task
from schemas import CreateTask, UpdateTask
from typing import Annotated
from backend.db_depends import get_db
from slugify import slugify
from models.user import User


router = APIRouter(prefix = '/task', tags = ['task'])

@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks

@router.get('/{task_id}')
async def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = 'Task was not found'
        )
    return task

@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], task_create: CreateTask, user_id: int ):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = 'User was not found'
        )
    db.execute(insert(Task).values(title = task_create.title,
                                   content = task_create.content,
                                   priority = task_create.priority,
                                   user_id = user_id,
                                   slug = slugify(str(user_id) + '/' + task_create.title)))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Create was successful'
    }

@router.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)], task_update: UpdateTask, task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = 'Task was not found'
        )
    db.execute(update(Task).where(Task.id == task_id).values(title = task_update.title,
                                   content = task_update.content,
                                   priority = task_update.priority
                                   ))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Update was successful'
    }

@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found'
        )
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Delete was successful'
    }

@router.delete('/delete_all')
async def delete_all_tasks(db: Annotated[Session, Depends(get_db)]):
    db.execute(delete(Task))
    db.commit()

    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Delete was successful'
    }