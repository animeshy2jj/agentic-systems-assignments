from fastapi import Request
from fastapi.responses import JSONResponse

async def custom_404_handler(request: Request, exc):
    return JSONResponse(
        status_code=404,
        content={
            "message": "The requested resource was not found"
        }
    )