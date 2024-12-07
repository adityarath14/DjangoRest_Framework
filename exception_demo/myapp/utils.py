from rest_framework.views import exception_handler
def custom_exception_handler(exc,context):
    response=exception_handler(exc,context)
    if response is not None:
        response.data['status_code']=response.status_code
        response.data['error_message']=str(exc)
        response.data['custom_info']='This is a custom error response.'
    return response