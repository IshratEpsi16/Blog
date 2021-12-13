from django.urls import path
from . import views
app_name = 'App_Login'
urlpatterns = [
    path('signup/',views.sign_up, name='signup'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('user_profile/',views.user_profile,name='user_profile'),
    path('add-picture/',views.add_pro_pic,name='add_pro_pic'),
    path('change-picture/',views.change_pro_pic,name='change_pro_pic'),

]