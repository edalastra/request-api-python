from cerberus import Validator

def get_users_validator(request: any):
    ''' Validate the request '''
    query_param_validator = Validator({
        'page': {'type': 'string', 'allowed': ['1','2','3','4'] ,'required': True},
    })

    response = query_param_validator.validate(request.query_params)
    if response is False:
        raise Exception(query_param_validator.errors)
