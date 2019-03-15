from django.urls import path
from . import views 
# from django.contrib.auth import login


urlpatterns =  [
    path('',views.index,name ='index'),
    # path('todo/<author_id>',views.todo,name ='todo'),
    path('todo/',views.todo,name ='todo'),
    path('delete/<int:id>',views.delete),
    path('login/',views.login_view,name="login"),
    path('signup/',views.register,name="signup"),
    path('logout/',views.logout_view,name="logout"),
    # path('login/',login,{'template_name':'todo/login.html'}),


   
    
]
