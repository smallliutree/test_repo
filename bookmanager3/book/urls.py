from django.urls import path
from book.views import index, readbook, login, login_json, header

urlpatterns = [
    path('index/',index),
    path('<cat_id>/<book_id>/',readbook),
    path('login/',login),
    path('login_json/',login_json),
    path('header/',header)
]