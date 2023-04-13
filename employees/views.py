from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Member
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import Task

def employees(request):
    return HttpResponse("EMPLOYEE DASHBOARD")


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


