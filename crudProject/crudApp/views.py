from django.shortcuts import render, redirect
from  .models import Article
from .forms import PostArticle
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
     if request.user.is_authenticated:
          return redirect('show')
     if request.method=="POST":
          username=request.POST["username"]
          email=request.POST["email"]
          password=request.POST["password"]
          user= User.objects.create_user(username, email, password)
          return redirect("login_user")
     #return redirect("login_user")
     return render(request,'crud/register.html')

def login_user(request):
     if request.method=="POST":
          username=request.POST["username"]
          password=request.POST["password"]
          user= authenticate(request,username=username, password=password)
          if user is None:
                return render(request,'crud/login.html')
          login(request, user)
          return redirect('/crud')

     return render(request,'crud/login.html')

def logout_user(request):
     if request.user.is_authenticated:
          logout(request)
          # Redirect to a success page.
          return redirect('login_user')
     return redirect('login_user')

    

def home(request):
    return render(request,'crud/index.html')

@login_required
def show(request):
    articles=Article.objects.all()
    return render(request,'crud/show.html',{'articles':articles})

@login_required   
def addArticle(request,id=0):
     if request.method=="GET":
          if id==0:
               form= PostArticle()
          else:
               article=Article.objects.get(pk=id)
               form=PostArticle(instance=article)
          return render(request,'crud/add.html',{'form':form})
     else:
          if  id==0:
               form= PostArticle(request.POST)
          else:
               article=Article.objects.get(pk=id)
               form=PostArticle(request.POST,instance=article)

          if form.is_valid():
               form.save()
          return redirect('/crud')

@login_required
def deleteArticle(request,id):
      article=Article.objects.get(pk=id)
      article.delete()
      return redirect('/crud')
