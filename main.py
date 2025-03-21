from fastapi import FastAPI
from app.routes import router

app = FastAPI()

# API marshrutlarini ulash
app.include_router(router)