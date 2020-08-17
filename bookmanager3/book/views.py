from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):

    return HttpResponse('ok')

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