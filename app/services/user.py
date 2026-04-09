from app.schemas.user import UserCreate
from app.models.user import user_collection

async def user_signup(user: UserCreate):
    user_dict = user.dict()
    is_email_exists = await user_collection.find_one({"email": user_dict["email"]})
    if is_email_exists:
        return {"success": False, "message": "Email already exists"}
    result = await user_collection.insert_one(user_dict)
    user_dict["_id"] = str(result.inserted_id)
    return  {"success": True, "data": user_dict}