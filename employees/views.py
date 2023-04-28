from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Member
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import Task , Member , Managers
import json
from datetime import datetime


def verifyUser(request, username, user_type):
    # username = request.COOKIES["username"]
    password = request.COOKIES["password"]
    print( "the password is " , password )
    print("username is " , username)
    print("here")

    if user_type == "manager":
        data = Managers.objects.filter(username = username).values()
    elif user_type == "employee":
        data = Member.objects.filter(username = username).values()

    if len(data) > 0:
        real_password = data[0]["password"]
        if password == real_password :
            return True 
    return False


def employees(request, username, status = "assigned"):

    if verifyUser(request, username, "employee"):

        data = Member.objects.filter( username = username ).values()[0]
        user_id = data["id"]

        print("the status is " , status)

        assigned = Task.objects.all().filter( assigned_to = user_id )
        in_progress = Task.objects.all().filter( assigned_to = user_id, status = "in_progress")
        pending = Task.objects.all().filter( assigned_to = user_id , due_date__lt = datetime.today()  ).exclude( status = "completed" )
        completed = Task.objects.all().filter( assigned_to = user_id , status = "completed"  ).order_by("-completed_date")


        user_data = {"username" : request.session["user_data"]["username"] , "type": "employee"}

        if status == "assigned":
            currentTitle = "Assigned"
            tasks = list(assigned)

        elif status == "in_progress":
            currentTitle = "In Progress"
            tasks =  list(in_progress)
        elif status == "pending":
            currentTitle = "Pending"
            tasks = list(pending)
            # date = datetime.today().strftime('%Y-%m-%d')
            # print(date, tasks)
        elif status == "completed":
            currentTitle = "Completed"
            tasks = list(completed)
        return render(request, "employee_dashboard.html" , {"tasks": tasks , "data": data  , "assigned_count":len(assigned) , "in_progress_count": len(in_progress) , "pending_count": len(pending) , "completed_count": len(completed) , "user_data": user_data , "currentTitle" : currentTitle })
        

    else:
        return redirect("/")

def manager(request , username , status = "assigned"):
    print("manager fuction")
    if verifyUser(request , username, "manager"):
        data = Managers.objects.filter( username = username ).values()[0]
        user_id = data['id']

        assigned = Task.objects.all().filter( assigned_by = user_id )
        in_progress = Task.objects.all().filter( assigned_by = user_id , status = "in_progress")
        pending = Task.objects.all().filter( assigned_by = user_id , due_date__lt = datetime.today()   )
        completed = Task.objects.all().filter( assigned_by = user_id , due_date__lt = datetime.today() , status = "completed" )

        new_tasks = Task.objects.all().filter(status = "completed" , manager_approved =  False)

        print("status is" , status)

        if status == "assigned":
            tasks =  list(assigned)
            currentTitle = "Assigned"
     
        elif status == "in_progress":
            currentTitle = "In Progress"
            tasks = list(in_progress)

        elif status == "pending":
            currentTitle = "Pending"
            tasks = list(pending)

        elif status == "completed":
            Task.objects.filter(status = "completed" ).update(manager_approved = True)
            print("changed manager verification")
            currentTitle = "Completed"
            tasks = list(completed)

        print(tasks)


        return render(request, "manager_dashboard.html" , {"tasks": tasks , "data": data  , "assigned_count":len(assigned) , "in_progress_count": len(in_progress) , "pending_count": len(pending) , "completed_count": len(completed) , "currentTitle" :currentTitle , "status": status, "new_task_count": len(new_tasks) }, )
        
    else:
        return HttpResponse("not signed in")
    
def manager_operations(request):
    
    data = json.load(request);
    print(data)
    if verifyUser(request , request.session["user_data"]["username"] , "manager" ):
        title = data["title"]
        description = data["description"]
        assigned_to =  data["assigned_to"]

        date = data["date"]

        check_member =  Member.objects.filter(username = assigned_to)
        assigned_to = Member.objects.get( username = assigned_to )

        print("assigned to value is" , type(assigned_to))

        assigned_by = request.session["user_data"]["id"]

        assigned_by  = Managers.objects.get( id = assigned_by)

        if title!="" and description != "" and len(check_member.values()) > 0 and date != "":

            
            # assigned_to_id = assigned_to[0]["id"]
            print(date)
            # date = "-".join(date.split("-")[::-1])

            task = Task( title = title , description = description , assigned_to = assigned_to , due_date= date, assigned_by = assigned_by, status = "assigned")
            task.save()
            return HttpResponse("done")
        else:
            return HttpResponse("not done")
    else:
        return HttpResponse("not done")

def employee_operations(request):
    
    # print( request.session["user_data"]["username"])
    # data = json.load(request, "employee")
    data = json.load(request)
    print(data)
    print(request.COOKIES["password"])
    username = request.session["user_data"]["username"]
    print("22the username is " , username)
    if verifyUser(request, username , "employee"):

        type = data["type"]

        if type == "update":

            status =  data["status"]
            if status == "completed":
                Task.objects.filter(id =  data["id"]).update( status = data['status'] , completed_date = datetime.today())
            elif status == "assigned" or status == "in_progress":
                Task.objects.filter(id =  data["id"]).update( status = data['status'] , completed_date = None , manager_approved =  False)

            print( "status is " , data['status'])
            print("here")
            return HttpResponse("done")
        

    return HttpResponse("not done")

def operations(request):
    data = json.load(request)
    if verifyUser(request , request.session["user_data"]["username"] , data["type"] ):
        pass




