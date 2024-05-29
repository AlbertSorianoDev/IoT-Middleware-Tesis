from fastapi import FastAPI
from fastapi.responses import JSONResponse

api_v1 = FastAPI()
api_v1.title = "IoT Middleware Suite API v1"
api_v1.version = "0.0.1"


@api_v1.get("/", tags=["Index"], include_in_schema=False)
async def index():
    return JSONResponse(
        content={"message": "Welcome to IoT Middleware Suite API v1"}, status_code=200
    )
