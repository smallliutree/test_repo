from django.urls import path, converters
from book.views import index, readbook, login, login_json, header, detail, json_response, to_index
from book import views

class MobilConverter:
    regex='1[3-9]\d{9}'

    def to_python(self, value):
        return value


converters.register_converter(MobilConverter, 'mobile')

urlpatterns = [
    path('index/',index),
    # path('<cat_id>/<book_id>/',readbook),
    path('login/',login),
    path('login_json/',login_json),
    path('header/',header),
    path('detail/',detail),
    path('json_response/',json_response),
    path('to_index/',to_index),

    path('p/<int:tieba_id>/',views.baidu_tieba),
    path('register/<mobile:phone>/',views.register),
    path('new_login/',views.new_login),
]