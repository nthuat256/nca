from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.cars import cars
from schemas.cars import CarCreate

def get_cars(db: Session):
    return db.query(cars).all()

def get_cars_by_id(db: Session, user_id: int):
    user = db.query(cars).filter(cars.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="user not found")

    return user

def create(db: Session, data: CarCreate):
    user = cars(
        name=data.name,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def delete(db: Session, user_id: int):
    user = get_cars_by_id(db, user_id)

    db.delete(user)
    db.commit()

    return {"message": "đã xóa thành công"}
