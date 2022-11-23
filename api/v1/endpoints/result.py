from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.__all_models import *
from schemas.__all_schemas import *
from core.deps import get_session

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED,
            response_model=ResultSchema)
async def post_result(result: ResultSchema,
                    db: AsyncSession = Depends(get_session)):
    pass
    # new_user = UserModel(fullname = user.fullname)
    # db.add(new_user)
    # await db.commit()
    # return new_user

@router.get('/', response_model=List[ResultSchema],
            status_code=status.HTTP_200_OK)
async def get_results(db: AsyncSession = Depends(get_session)):
    pass
    # async with db as session:
    #     query = select(UserModel)
    #     result = await session.execute(query)
    #     cursos: List[UserModel] = result.scalars().all()
    #     return cursos

@router.get('/{result_id}', 
            response_model=ResultSchema, 
            status_code=status.HTTP_200_OK)
async def get_result(result_id: int, 
                    db: AsyncSession = Depends(get_session)):
    pass
    # async with db as session:
    #     query = select(UserModel).filter(UserModel.id == user_id)
    #     result = await session.execute(query)
    #     curso = result.scalar_one_or_none()
    #     if curso:
    #         return curso
    #     else:
    #         raise(HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
    #                             detail="Aposta não encontrada..."))

@router.put('/{result_id}', 
            response_model=ResultSchema, 
            status_code=status.HTTP_202_ACCEPTED)
async def put_result(result_id: int, result: ResultSchema,
                    db: AsyncSession = Depends(get_session)):
    pass
    # async with db as session:
    #     query = select(UserModel).filter(UserModel.id == user_id)
    #     result = await session.execute(query)
    #     curso_up = result.scalar_one_or_none()
    #     if curso_up:
    #         curso_up.fullname = user.fullname
    #         await session.commit()
    #         return curso_up
    #     else:
    #         raise(HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
    #                             detail="Aposta não encontrada..."))

@router.delete('/{result_id}',  
            status_code=status.HTTP_204_NO_CONTENT)
async def delete_result(result_id: int, result: ResultSchema,
                    db: AsyncSession = Depends(get_session)):
    pass
    # async with db as session:
    #     query = select(UserModel).filter(UserModel.id == user_id)
    #     result = await session.execute(query)
    #     curso_del = result.scalar_one_or_none()
    #     if curso_del:
    #         await session.delete(curso_del)
    #         await session.commit()
    #         return Response(status_code=status.HTTP_204_NO_CONTENT)
    #     else:
    #         raise(HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
    #                             detail="Aposta não encontrada..."))

