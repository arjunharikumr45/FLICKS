from django.urls import path
from .import views
from .views import logout_view


urlpatterns  = [
 path("",views.home_new,name='home'),
 path('signup/',views.signup_view,name='signup'),
 path('login/',views.login_view,name='login'),
 path('terms/',views.terms),
 path('subs/',views.subs,name='subscription'),
 path('pay/',views.pay,name='payment'),
#  path('home_2/',views.home2),
 path('action/', views.action, name='action'),
   path('signup/', views.signup_view, name='signup'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
]