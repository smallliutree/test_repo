from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.
def index(request):

    return HttpResponse('ok')


def readbook(requset, cat_id, book_id):
    content = f'cat:{cat_id}, book:{book_id}'

    print(requset.GET)
    keyword = requset.GET.getlist('keyword')
    print(keyword)

    return HttpResponse('ok')


def login(requset):
    print(requset.POST)

    return HttpResponse('login')


def login_json(request):
    body = request.body
    body_str = body.decode()
    print(body_str)

    import json
    body_dict = json.loads(body_str)
    print(body_dict)

    return HttpResponse('json')


'''
查询练习
'''
from book.models import BookInfo, PeopleInfo

book = BookInfo.objects.get(id=1)
book.peopleinfo_set.all()

person = PeopleInfo.objects.get(id=1)
person.book

BookInfo.objects.filter(peopleinfo__name__exact='郭靖')
BookInfo.objects.filter(peopleinfo__description__contains='八')

PeopleInfo.objects.filter(book__name='天龙八部')
PeopleInfo.objects.filter(book__readcount__gt=30)