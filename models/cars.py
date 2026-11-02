from sqlalchemy import Column,INTEGER,String,Float,ForeignKey
from core.database import Base
class car_types(Base):
    __tablename__='car_types'
    car_type_id=Column(INTEGER,primary_key=True,index=True)
    car_type_name=Column(String(100))
class cars(Base):
    __tablename__='car'
    id=Column(INTEGER,primary_key=True,index=True)
    car_code= Column(String(100))
    rental_price=Column(Float)
    car_type_id = Column(INTEGER, ForeignKey("car_types.car_type_id"))