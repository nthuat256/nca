
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.cars import CarCreate,CarResponse
from services import cars

router = APIRouter(
    prefix="/users",
    tags=["users"]
)
@router.post('/',response_model=CarResponse)
def add(data:CarCreate,db:Session=Depends(get_db)):
    return cars.create(data,db)

@router.get('/',response_model=list[CarResponse])
def get_cars(db:Session=Depends(get_db)):
    return cars.get_cars(db)

@router.delete('/{cars_id}',response_model=CarResponse)
def delete(cars_id:int,db:Session=Depends(get_db)):
    return cars.delete(cars_id,db)