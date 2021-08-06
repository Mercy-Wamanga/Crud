from django.urls import path, include
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
     path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login/',views.login_user,name="login_user"),
    path('logout/',views.logout_user,name="logout_user"),
    path('crud/',views.show,name="show"),
    path('add/',views.addArticle,name="postArticle"),
    path('<int:id>/',views.addArticle,name="updateArticle"),   
    path('delete/<int:id>/',views.deleteArticle,name="deleteArticle"),
]