from fastapi import APIRouter, Request as RequestFastAPI
from fastapi.responses import JSONResponse

from src.main.adapters.request_adapter import request_adapter
from src.validators import get_users_validator
from src.main.composers.get_users_composer import get_users_composer

users_routes = APIRouter()

@users_routes.get("/api/users/list")
async def get_users(request: RequestFastAPI):
    ''' Get all users '''

    get_users_validator(request)
    controller = get_users_composer()

    response = await request_adapter(request, controller.handle)

    return JSONResponse(
        status_code=response["status_code"],
        content=response['data']
    )
