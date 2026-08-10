from django.http import HttpResponse
class ExecutionFlow(object):
    def __init__(self,get_response):
        print('init method')
        self.get_response=get_response
    def __call__(self,request):
        print("processing the middleware")
        response=self.get_response(request)
        print("postprocessing the middleware")
        return response    
