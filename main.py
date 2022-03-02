from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from resources.routes import api_router
from config.db import database
from decouple import config

origins = [
  "http://localhost",
  "http://localhost:3000"
]


app = FastAPI(
  title = config('PROJECT_NAME'),
  openapi_url = f"{config('API_V1_STR')}/openapi.json"
)
app.include_router(api_router, prefix=config('API_V1_STR'))
app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

@app.on_event("startup")
async def startup():
  await database.connect()

@app.on_event("shutdown")
async def shutdown():
  await database.disconnect()