from django.http import HttpResponse
class AppMaintenance(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        response=self.get_response(request)
        return response
    def process_exception(self,request,execution):
        return HttpResponse(f"<h1 style='text-align:center;color:red;'>currently we are facing technical issues try after some time: {execution}</h1>")    