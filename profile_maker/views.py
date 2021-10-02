from django.shortcuts import render,redirect
from django.views.generic import ListView,DeleteView,UpdateView
from .models import mypeople
from .forms import pform
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy 
from .models import ytvideos
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

def uploadstuff(request):
    stuff = mypeople.objects.all()
    return render(request,'home.html',{stuff:'stuff'})

def real(request):
    if request.method == 'POST':
        form = pform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('realhome')
    else:
        form = pform()
    return render(request, 'home.html', {
        'form': form
    })


class home(ListView):
    model = mypeople
    template_name = 'realhome.html'
    context_object_name = 'mistermaker'


class ythome(ListView):
    model = ytvideos
    template_name = 'ythome.html'
    # paginate_by = 2  
    context_object_name = 'mistermaker'


@method_decorator(login_required, name='dispatch') 
class ytube(CreateView):
    model = ytvideos
    fields = '__all__'
    template_name = 'ytcreate.html'  

def hpage(request):
    return render(request,'hpage.html')



def loginuser(request):
     if request.method=='GET':
        return render(request,'loginuser.html',{'form':AuthenticationForm})
     else:
         user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
         if user is None:
             return render(request,'loginuser.html',{'form':AuthenticationForm,'error':'Either username does not exist or Password doesnot match the user name'})
         else:
             login(request,user)
             return redirect('hpage') 
    
def signupuser(request):
    if request.method=='GET':
        return render(request,'signup.html',{'form':UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('current')
            except IntegrityError:
                return render(request,'signup.html',{'form':UserCreationForm,'error':'Please Choose Another UserName!'})
@login_required
def logout(request):
    auth.logout(request)
    return render(request,'hpage.html')

