from django.shortcuts import render,redirect
from .forms import StudentRegistration
from .models import User
from django.http import JsonResponse

def home(request):
    form = StudentRegistration()
    users = User.objects.all()
    context = {
        'form': form,
        'users':users
    }
    return render(request,'enroll/main/home.html',context)

def save_data(request):
    if request.method == 'POST':
       form = StudentRegistration(request.POST)
       if form.is_valid():
           sid = request.POST['user_id']
           name = request.POST['name']
           email = request.POST['email']
           password = request.POST['password']
           if (sid == ''):
              usr = User(name=name, email=email, password=password)
           else:  
              usr = User(id=sid,name=name, email=email, password=password)
           usr.save()
           users = User.objects.values()
           users_data = list(users) 
           return JsonResponse({
               'status':'Save',
               'users_data':users_data,
               })
       else:
           return JsonResponse({
               'status':'Save'
               })
   
def delete_data(request):
    if request.method == 'POST':
         id = request.POST.get('sid')
         pi = User.objects.get(pk=id)
         pi.delete()
         return JsonResponse({
             'status':1,
         })
    else:
        return JsonResponse({
            'status':0,
        })

def edit_data(request):
    if request.method == 'POST':
       id = request.POST.get('sid')
       user = User.objects.get(pk=id)
       user_data = {
           "id":user.id,
           "name":user.name,
           "email":user.email,
           "password":user.password,
           }
        
       return JsonResponse(user_data)
