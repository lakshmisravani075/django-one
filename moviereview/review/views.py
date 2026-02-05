from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from review.models import movie_detials
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from review.models import Users




# Create your views here.


def basic(request):
    return HttpResponse("Hello world")
# for queryparams:
def movie_info(request):
    movie=request.GET.get("movie")
    date=request.GET.get("date")
    return JsonResponse({"status":"success", "result":{"movie_name":movie,"realse_date":date}},status=200)

# @csrf_exempt
# def movies(request):
#     if request.method =="POST":
        # data=json.loads(request.body)  
        #  data=request.POST.copy()     
        # print(data.get("movie_name"))
        
    # rating_value = int(data.get("rating"))
    # stars = "⭐" *rating_value
    # data["star"] = stars
    # print("POST Data:",data)
    # movie= movie_detials.objects.create(movie_name=data.get("movie_name"),date=data.get("date"), budget=data.get("budget"),rating=rating_value)
    # return JsonResponse({"status":"success" ,"message":"movie record inserted successfully" ,"data":data},status=200)

    # return JsonResponse({"error":"error occured"},status=400)
    
@csrf_exempt
def movies(request):
    if request.method=="GET":
        movie_info=movie_detials.objects.all()
        movie_list=[]
        for movie  in movie_info:
            movie_list.append({"movie_name":movie.movie_name,
                                "date":movie.date,
                                "budget":movie.budget,
                                "rating":movie.rating})
        return JsonResponse({"status":"success","data":movie_list},status=200)   
        
    
    elif request.method=="PUT":
        data=json.loads(request.body)
        # print("PUT data:",data)      check the incoming data      
        ref_id=data.get("id")
        # print("Reference_id:",ref_id)  check the id  coming from the client
        exsiting_movie=movie_detials.objects.get(id=ref_id)
        # print("Exsiting_movie:",exsiting_movie)  checking  the exsiting movie object fetching from db
        if data.get("movie_name"):
            new_movie_name=data.get("movie_name")
            exsiting_movie.movie_name=new_movie_name
            exsiting_movie.save()
        elif data.get("date"):
            new_date=data.get("date")
            exsiting_movie.date=new_date
            exsiting_movie.save()
            
        elif data.get("budget"):
            new_budget=data.get("budget")
            exsiting_movie.budget=new_budget
            exsiting_movie.save()
        elif data.get("rating"):
            new_rating=data.get("rating")
            exsiting_movie.rating=new_rating
            exsiting_movie.save()
            return JsonResponse({"status":"success","message":"movie updated  successfully","data":data},status=200)
        
        # elif request.method=="DELETE":
        #     data=request.GET.get("id")
        #     ref_id=int(data)
        #     exsiting_movie=movie_detials.objects.get(id=ref_id)
        #     exsiting_movie.delete()
        #     return JsonResponse({"status":"success","message":"movie record is deleted"},status=200)
        
        
@csrf_exempt
def signup(request):
    if request.method == "POST":
        data = request.POST

        username = data.get("username")
        password = data.get("password")
        email = data.get("email")

        # Check required fields
        if not username or not password:
            return JsonResponse({"status": "failed", "message": "username and password are required"}, status=400)

        # Check if user already exists
        if Users.objects.filter(username=username).exists():
            return JsonResponse({"status": "failed", "message": "username already exists"}, status=400)

        # Create user with hashed password
        try:
            user = Users(
                username=username,
                email=email,
                password=make_password(password)     # Hash the password
            )
            user.save()

            return JsonResponse({"status": "success", "message": "user created successfully"}, status=201)

        except Exception as e:
            return JsonResponse({"status": "failed", "message": str(e)}, status=400)









@csrf_exempt

def login(request):
    if request.method=="POST":
        data=request.POST
        print(data)
        username=data.get("username")
        password=data.get("password")
      
    try:
            
            user= Users.objects.get(username=username)
            if check_password(password,user.password):
                return JsonResponse({"status": "successfully loggin"},status=200)
            else:
                return JsonResponse({"status":"failed loggin", "message":"invalid password"},status=400)
    except Users.DoesNotExist:
             return JsonResponse({"status":"failure","message":"user not found"},status=400)

        








    
    



    

