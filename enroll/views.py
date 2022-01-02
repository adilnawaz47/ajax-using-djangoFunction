from django.shortcuts import render
from .models import *
from django.http  import JsonResponse
# Create your views here.
def home(request):
    stud = User.objects.all()
    return render(request, 'enroll/home.html', {'stu':stud})

def save_data(request):
    if request.method =="POST":
        sid = request.POST.get('stuid')
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        print(sid)
        if (sid == ""):
            usr = User(name=name, email=email, password=password)
        else:
            usr = User(id=sid,name=name, email=email, password=password)
        usr.save()
        stud = User.objects.values()
        return JsonResponse({'status':'save', 'student_data':list(stud)})
    else:
        return JsonResponse({'status':0})

def delete_data(request):
    if request.method =="POST":
        id = request.POST.get('sid')
        pi = User.objects.get(pk = id)
        pi.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})

# edit data
def edit_data(request):
    if request.method =="POST":
        id = request.POST.get('sid')
        student = User.objects.get(pk = id)
        student_data = {"id":student.id, "name":student.name, "email":student.email,"password":student.password }
        return JsonResponse(student_data)
    else:
        return JsonResponse({'status':'unable to store data'})