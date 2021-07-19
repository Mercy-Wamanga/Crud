from django.shortcuts import render , redirect
from .form import PostArticle
from  .models import Article



# Create your views here.
def home(request):
    articles=Article.objects.all()
    return render(request,'ariticle-page.html',{'articles':articles})


# Add an Article

def AddArticle(request):
     if request.method=='POST':
         fm=PostArticle(request.POST)
         if fm.is_valid():
            article = fm.save()
            article.save()
            return redirect('ariticle-page.html')
    #  else:
    #      fm=PostArticle()
    #  return render(request,'ariticle-page.html',{'form':fm})
     


