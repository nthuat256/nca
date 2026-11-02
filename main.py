from fastapi import FastAPI
from core.database import Base, engine
from routers.cars import router
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": 'API đang chạy'
    }

