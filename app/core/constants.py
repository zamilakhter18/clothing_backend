from enum import Enum

class Constants(str, Enum):
    SUCCESS = "Success"
    INVALID_CREDENTIALS = "Invalid credentials"
    EMAIL_ALREADY_EXISTS = "Email already exists"
    USER_NOT_FOUND = "User not found"
    USER_CREATED_SUCCESSFULLY = "User created successfully"
    USER_UPDATED_SUCCESSFULLY = "User updated successfully"
    USER_DELETED_SUCCESSFULLY = "User deleted successfully"
    USER_ALREADY_EXISTS = "User already exists"