from fastapi import APIRouter
from app.schemas.user import UserCreate
from app.services.user import user_signup
from app.core.response_handler import ResponseHandler
from app.core.constants import Constants

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/signup")
async def signup(user: UserCreate):
    try:
        result = await user_signup(user)
        if result["success"]:
            return ResponseHandler.success_response_with_data(
                Constants.USER_CREATED_SUCCESSFULLY,
                result["data"]
            )
        return ResponseHandler.error_response(result["message"])
    except Exception as e:
        return ResponseHandler.internal_error_response(str(e))