from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from src.api.v1.api_v1 import api_v1

tags_metadata = [
    {
        "name": "API v1 Documentation",
        "description": "API version 1. Check the docs at /api/v1/docs.",
    },
]

app = FastAPI(openapi_tags=tags_metadata)
app.title = "IoT Middleware Suite Service"
app.version = "1.0.0"


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/api/v1", api_v1)


@app.get("/", tags=["Index"], include_in_schema=False)
async def index():
    return JSONResponse(
        content={"message": "Welcome to IoT Middleware Suite Service"}, status_code=200
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
