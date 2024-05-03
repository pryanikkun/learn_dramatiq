import asyncio

import uvicorn
from fastapi import FastAPI
from messages.views import msg_router

app = FastAPI(
    title="TG and FastApi"
)

app.include_router(msg_router)


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)





