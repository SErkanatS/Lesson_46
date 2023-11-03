from django.urls import path
from .views import RegisterView, Login, Dashboard, Logout, UnderAge

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('signup/', RegisterView.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('underage_page/', UnderAge.as_view(), name='underage_page'),
]