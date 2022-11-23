from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.__all_models import *
from schemas.__all_schemas import *
from core.deps import get_session

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED,
            response_model=BetSchema)
async def post_bet(bet: BetSchema,
                    db: AsyncSession = Depends(get_session)):
    new_bet = BetModel(firstTeam= bet.firstTeam, 
    secondTeam= bet.secondTeam, firstTeamQuantyGoals= bet.firstTeamQuantyGoals,
    secondTeamQuantyGoals= bet.secondTeamQuantyGoals, user=bet.user)

    db.add(new_bet)
    await db.commit()
    return new_bet

@router.get('/', response_model=List[BetSchema],
            status_code=status.HTTP_200_OK)
async def get_bets(db: AsyncSession = Depends(get_session)):
    pass
    # async with db as session:
    #     query = select(UserModel)
    #     result = await session.execute(query)
    #     cursos: List[UserModel] = result.scalars().all()
    #     return cursos

@router.get('/{bet_id}', 
            response_model=BetSchema, 
            status_code=status.HTTP_200_OK)
async def get_bet(bet_id: int, 
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

@router.put('/{bet_id}', 
            response_model=BetSchema, 
            status_code=status.HTTP_202_ACCEPTED)
async def put_bet(bet_id: int, bet: BetSchema,
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

@router.delete('/{bet_id}',  
            status_code=status.HTTP_204_NO_CONTENT)
async def delete_bet(bet_id: int, bet: BetSchema,
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

