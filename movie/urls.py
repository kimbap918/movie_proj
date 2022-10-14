from django.urls import path 
from . import views

app_name = "movie"

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('accounts/', views.accounts, name='accounts'),
    path('detail/<int:pk>/', views.detail, name="detail"),
    path('update/', views.update, name='update'),
]
