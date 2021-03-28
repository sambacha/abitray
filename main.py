import uvicorn
from fastapi import FastAPI
# from api.v1.api import api_router
import config

from app.api import api
from app.database import database

app = FastAPI()
app.include_router(api)
#app.include_router(api_router)

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

if __name__ == "__main__":
    uvicorn.run(app, host=config.SERVER_IP, port=config.SERVER_PORT)

