from contextlib import asynccontextmanager
from venv import create

from fastapi import FastAPI, Request

resource = {}

@asynccontextmanager
async def app_lifespan(app: FastAPI):
    # uncomment me to show changes
    # raise KeyError("err nerr")
    print("init lifespan")
    resource["msg"] = "Hello, lil brudder!"
    yield
    resource.clear()
    print("clean up lifespan")

def create_app():
    app = FastAPI(lifespan=app_lifespan)

    @app.get("/", include_in_schema=False)
    async def root(request: Request):
        return resource["msg"]

    print("completed app init.")
    return app
