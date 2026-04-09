from fastapi import FastAPI
from app.routes import user
from fastapi.exceptions import RequestValidationError
from app.core.exceptions import validation_exception_handler

app = FastAPI(swagger_ui_parameters={"defaultModelsExpandDepth": -1})

# register handler
app.add_exception_handler(RequestValidationError, validation_exception_handler)

# register routes
app.include_router(user.router, prefix="/api")