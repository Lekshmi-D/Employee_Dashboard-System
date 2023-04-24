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

        if status == "assigned":
            tasks =  Task.objects.all().filter( assigned_to = user_id)
            
            # tasks = Task.objects.raw(f"select employees_task.id , title , due_date , description , employees_managers.username from employees_task , employees_managers where employees_task.assigned_to = {user_id} and status = 'assigned' and employees_task.assigned_by = employees_managers.id"  )
            print("the tasks are ", tasks[0].assigned_by.username)

        elif status == "in_progress":
            tasks =  Task.objects.filter( assigned_to = user_id , status = "in_progress").values()
        elif status == "pending":
            # date = datetime.today().strftime('%Y-%m-%d')
            tasks =  Task.objects.filter( assigned_by = user_id , due_date__lt = datetime.today()  ).values()
            # print(date, tasks)
        elif status == "completed":
            tasks =  Task.objects.filter( assigned_to = user_id , status = "completed").values()
        
        print(tasks)

        return render(request, "employee_dashboard.html" , {"tasks": list(tasks) , "data": data })
    else:
        return redirect("/")

def manager(request , username , status = "assigned"):
    print("manager fuction")
    if verifyUser(request , username, "manager"):
        data = Managers.objects.filter( username = username ).values()[0]
        user_id = data['id']


        if status == "assigned":
            tasks =  Task.objects.filter( assigned_by = user_id).values()
            # tasks = Task.objects.raw("select * from employees_task , emplo")
        elif status == "in_progress":
            tasks =  Task.objects.filter( assigned_by = user_id , status = "in_progress").values()
        elif status == "pending":
            # sdate = datetime.today().strptime("%Y-%m-%d")
            # sprint(date)
            # sprint(Task.objects.filter(assigned_by  = user_id).values())
            tasks =  Task.objects.filter( assigned_by = user_id , due_date__lt = datetime.today()  ).values()

        elif status == "completed":
            tasks =  Task.objects.filter( assigned_by = user_id , status = "completed").values() 

        return render(request, "manager_dashboard.html" , {"tasks": list(tasks) , "data": data })
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



def operations(request):
    
    # print( request.session["user_data"]["username"])
    # data = json.load(request, "employee")
    data = json.load(request)
    print(data)
    print(request.COOKIES["password"])
    username = request.session["user_data"]["username"]
    print("22the username is " , username)
    if verifyUser(request, username , "employee"):
        print( "status is " , data['status'])
        Task.objects.filter(id =  data["id"]).update( status = data['status'])
        print("here")
        # Task.objects.get(id =  data["id"])
        # Task.status =   data['status']
        # Task.save()
        return HttpResponse("done")
    return HttpResponse("not done")



'''def index(request):
    labels=[]     #for names
    data=[]       #for salary

    queryset=Member.objects.order_by('-salary')[:5]
    for person in queryset:
        labels.append(person.firstname)
        data.append(person.salary)

    return render(request,'index.html',{
        'labels':labels,
        'data': data
    })'''


class MemberChart(TemplateView):
    template_name = 'charts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Member.objects.all()
        return context

@login_required()
def task_list(request):                        #to display the task
    tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})

@login_required
def update_task(request, pk):                 #to update status of a task
    task = get_object_or_404(Task, pk=pk, assigned_to=request.user)
    if request.method == 'POST':
        task.status = request.POST.get('status')
        task.save()
        return redirect('task_list')
    return render(request, 'update_task.html', {'task': task})
# Create your views here.


