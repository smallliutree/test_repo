from django.urls import path
from book.views import index, readbook, login

urlpatterns = [
    path('index/',index),
    path('<cat_id>/<book_id>/',readbook),
    path('login/',login)
]