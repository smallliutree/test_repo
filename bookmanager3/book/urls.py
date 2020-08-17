from django.urls import path
from book.views import index, readbook

urlpatterns = [
    path('index/',index),
    path('<cat_id>/<book_id>/',readbook),
]