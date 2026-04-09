from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import Request


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # first error message from the list of errors
    error_message = exc.errors()[0]["msg"]

    return JSONResponse(
        status_code=400,
        content={
            "statusCode": 400,
            "message": error_message
        }
    )