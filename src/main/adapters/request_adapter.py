from typing import Callable
from fastapi import Request as RequestFastAPI


async def request_adapter(request: RequestFastAPI, callback: Callable):
    ''' Adapter to convert the request to a dict '''
    body = None

    try:
        body = await request.json()
    except:
        pass

    http_request = {
        'query_params': request.query_params,
        'body': body,
    }
    try:
        http_response = callback(http_request)
        return http_response
    except:
        print('Error in request_adapter')
