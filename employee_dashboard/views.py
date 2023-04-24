from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from django.template import RequestContext

from employees.models import Member, Managers

from employees.views import verifyUser

def signin(request):

    if "password" in request.COOKIES and "username" in request.COOKIES and "member_type" in request.COOKIES :

        username = request.COOKIES["username"]
        member_type = request.COOKIES["member_type"]

        if verifyUser(request , username ,  member_type ):
            print("user already signed in")
            print(dict(request.session))

            if member_type == "manager":
                response =  redirect(f"/manager/{username}")
                return response
            elif member_type == "employee":
                response = redirect(f"/employees/{username}")
                return response

    if request.method == "POST":
  
        username = request.POST["username"]
        password = request.POST["password"]
        member_type = request.POST["type"]

        if member_type ==  "employee":
            data = Member.objects.filter(username= username).values()
        elif member_type == "manager":
            data = Managers.objects.filter(username = username).values() 

        print("going to sign in")
        print(data)
        if(len(data) > 0 ):
            real_password = data[0]["password"]
            print(password , real_password)
            print(username, password)
            if real_password == password  :
                print("here")
                request.session["user_data"] = list(data)[0]
                if member_type == "employee":
                    response = redirect(f"/employees/{username}")
                    response.set_cookie("username", username)
                    response.set_cookie("password" ,password)
                    response.set_cookie("member_type" , member_type)
                    return response
                    # return render(request , "employee_dashboard.html" , {"data" : data[0]} )
                elif member_type == "manager":
                    print("hereeee")
                    response =  redirect(f"/manager/{username}")
                    response.set_cookie("username" , username)
                    response.set_cookie("password" , password)
                    response.set_cookie("member_type" , member_type)
                    print("here2")
                    return response
            else:
                 return render(request , "signin.html", {"warning" : "incorrect username of password"})
        else:
            return render(request , "signin.html", {"warning" : "user does not exist"})



       

    else:
        return render(request ,"signin.html", {"warning":""}  )
    

def signout(request):
    response = redirect("/")
    response.delete_cookie("username" )
    response.delete_cookie("password")
    response.delete_cookie("member_type")
    return response