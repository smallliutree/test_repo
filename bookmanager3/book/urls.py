from django.urls import path
from book.views import index, readbook, login, login_json, header, detail, json_response

urlpatterns = [
    path('index/',index),
    path('<cat_id>/<book_id>/',readbook),
    path('login/',login),
    path('login_json/',login_json),
    path('header/',header),
    path('detail/',detail),
    path('json_response/',json_response),
]