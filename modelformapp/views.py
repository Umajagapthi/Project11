from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from.forms import RegForm,LoginForm
from.models import Reg
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class RegInput(View):
    def get(self,request):
        r_f=RegForm()
        return render(request,'reginput.html',{'reg_form':r_f})
class RegInsert(View):
    def post(self, request):
        r_f=RegForm(request.POST)
        if r_f.is_valid():
            r_f.save()
        return HttpResponse("registration successful")
class LoginInput(View):
    def get(self,request):
        l_f=LoginForm()
        return render(request,'logininput.html',{'login_form':l_f})
class LoginVerf(View):
    def post(self,request):
        MyLoginForm=LoginForm(request.POST)
        if MyLoginForm.is_valid():
            user=MyLoginForm.cleaned_data['username']
            password=MyLoginForm.cleaned_data['password']
            dbuser=Reg.objects.filter(username=user,password=password)
            if not dbuser:
                return HttpResponse("loginfailed")
            else:
                return HttpResponse("login successful")