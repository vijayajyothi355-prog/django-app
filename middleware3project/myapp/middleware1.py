from django.http import HttpResponse
class AppMaintenanceMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        response=self.get_response(request)
        return response
    def process_exception(self,request,exception):
        return HttpResponse(f"<h1 style='text-align:center;color:blue;'>currently we are facing technical issues try after some time: {exception}</h1>") 
  