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
    path('logout/', views.logout, name='logout'),
    path('create/', views.create, name='create'),
    path('community/', views.community, name='community'),
    path('review_detail/<int:pk>/', views.review_detail, name='review_detail'),
    path('review_udate/<int:pk>', views.review_update, name='review_update'),
]
