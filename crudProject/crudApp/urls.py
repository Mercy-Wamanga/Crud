from django.urls import path, include
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.show),
    path('add/',views.addArticle,name="postArticle"),
    path('<int:id>/',views.addArticle,name="updateArticle"),   
    path('delete/<int:id>/',views.deleteArticle,name="deleteArticle"),
]