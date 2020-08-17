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