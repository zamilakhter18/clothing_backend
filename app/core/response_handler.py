from fastapi.responses import JSONResponse


class ResponseHandler:

    @staticmethod
    def success_response(msg: str):
        return JSONResponse(
            status_code=200,
            content={
                "status_code": 200,
                "message": msg
            }
        )

    @staticmethod
    def success_response_with_data(msg: str, data):
        return JSONResponse(
            status_code=200,
            content={
                "status_code": 200,
                "message": msg,
                "data": data
            }
        )

    @staticmethod
    def success_response_with_token(msg: str, token: str):
        return JSONResponse(
            status_code=200,
            content={
                "status_code": 200,
                "message": msg,
                "token": token
            }
        )

    @staticmethod
    def success_response_with_data_and_token(msg: str, data, token: str):
        return JSONResponse(
            status_code=200,
            content={
                "status_code": 200,
                "message": msg,
                "data": data,
                "token": token
            }
        )

    @staticmethod
    def error_response(msg: str):
        return JSONResponse(
            status_code=400,
            content={
                "status_code": 400,
                "message": msg
            }
        )

    @staticmethod
    def error_response_with_data(msg: str, data):
        return JSONResponse(
            status_code=400,
            content={
                "status_code": 400,
                "message": msg,
                "data": data
            }
        )

    @staticmethod
    def unauthorized_response(msg: str):
        return JSONResponse(
            status_code=401,
            content={
                "status_code": 401,
                "message": msg
            }
        )

    @staticmethod
    def internal_error_response(msg: str):
        return JSONResponse(
            status_code=500,
            content={
                "status_code": 500,
                "message": msg
            }
        )