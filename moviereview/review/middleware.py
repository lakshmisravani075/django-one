from django.http import JsonResponse
from django.http import HttpResponse
 
#  to check  the  middelware  is working  particular url  or  not
# class MovieReviewMiddleware:
#     def __init__(self,get_response):
#         self.get_response=get_response
#     def __call__(self,request):
#         if request.path=="/movies/":
#          print("movies api is called")
#         return self.get_response(request)  
            
            
            
class MovieReviewMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if request.path=="/movies/" and request.method=="POST":
            incoming_data=request.POST 
            print("incoming_data:",incoming_data)
        
#to  check  that  if  the key  is  present in data  or not
            if not incoming_data.get("rating"):
                return JsonResponse({"error":"rating  is  required"},status=400)
            elif float(incoming_data.get("rating"))<0 or float(incoming_data.get("rating"))>5:
                return JsonResponse({"error":"rating should be b/w 0 to 5"},status=400)
            elif not incoming_data.get("budget"):
                return JsonResponse({"error":"budget is required"},status=400)
            elif not incoming_data.get("date"):
                return JsonResponse({"error":"date  is  required"},status=400)
            elif not incoming_data.get("movie_name"):
                return JsonResponse({"error":"movie_name is  required"},status=400)
        return self.get_response(request)