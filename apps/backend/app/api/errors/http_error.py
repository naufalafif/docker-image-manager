from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse


async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    """
    This is an asynchronous Python function that handles HTTP exceptions by returning a JSON response
    with the error message and status code.
    """
    return JSONResponse({"errors": [exc.detail]}, status_code=exc.status_code)
