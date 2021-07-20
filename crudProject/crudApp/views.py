from django.shortcuts import render, redirect
from  .models import Article
from .forms import PostArticle


# Create your views here.

def show(request):
    articles=Article.objects.all()
    return render(request,'crud/show.html',{'articles':articles})
    
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


def deleteArticle(request,id):
      article=Article.objects.get(pk=id)
      article.delete()
      return redirect('/crud')
