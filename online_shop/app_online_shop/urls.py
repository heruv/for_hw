from django.urls import path
from .views import index, top_sellers, advertisment, login, profile, register

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisment/', advertisment, name='advertisement'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register')
]
