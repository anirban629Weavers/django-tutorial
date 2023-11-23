from django.urls import path
from .views import register,home,login,registerAdmin,loginAdmin

urlpatterns = [
    path('', home,name="home"),
    path('register/', register,name="register"),
    path('login/', login,name="login"),
    path('register-admin/', registerAdmin,name="register"),
    path('login-admin/', loginAdmin,name="login"),
]


