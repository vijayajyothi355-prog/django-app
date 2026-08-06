from django.http import HttpResponse
class AppMaintenanceMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        return HttpResponse("<h1 style='text-align:center;color:brown'>currently app is under maintenance</h1>")     