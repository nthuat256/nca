from pydantic import BaseModel

class CarCreate(BaseModel):
    car_code:str
    rental_price:float
    car_type_id:int
class CarResponse(BaseModel):
    id:int
    car_code:str
    rental_price:float
    car_type_id:int
    car_type_name:str
class ConFig:
    from_attributes=True