from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):

    return HttpResponse('ok')

'''
增删改查练习
'''
from book.models import BookInfo

book = BookInfo(
    name='葵花宝典',
    pub_date='2012-10-8',
    readcount=100
)
book.save()

book = BookInfo.objects.create(
    name='django',
    pub_date='2005-1-1',
    readcount='654',
    commentcount='123'
)


book = BookInfo.objects.get(id=6)
book.name = 'flask'
book.readcount = 369
book.save()

BookInfo.objects.filter(id=6).update(
    name='爬虫',
    readcount=457,
    commentcount=852,
    pub_date='2020-1-1'
)


book = BookInfo.objects.get(id=6)
book.delete()

BookInfo.objects.get(id=5).delete()


book = BookInfo.objects.get(id=3)
BookInfo.objects.all()


BookInfo.objects.get(id__exact=1)
BookInfo.objects.get(name__contains='湖')
BookInfo.objects.get(name__endswith='部')
BookInfo.objects.filter(name__isnull=True)
BookInfo.objects.filter(id__in=[1, 3, 5])
BookInfo.objects.filter(id__gt=3)
BookInfo.objects.filter(pub_date__year=1980)
BookInfo.objects.filter(pub_date__gt='1990-1-1')


from django.db.models import F
BookInfo.objects.filter(readcount__gte=F('commentcount'))
BookInfo.objects.filter(readcount__gt=20, id__lt=3)

from django.db.models import Q
BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))
BookInfo.objects.filter(~Q(id__exact=3))
BookInfo.objects.exclude(id=3)


from django.db.models import Max, Min, Avg, Count, Sum
BookInfo.objects.aggregate(Sum('readcount'))
BookInfo.objects.all().order_by('readcount')
BookInfo.objects.all().order_by('-readcount')


book = BookInfo.objects.get(id=1)
book.peopleinfo_set.all()
from book.models import PeopleInfo
person = PeopleInfo.objects.get(id=18)
person.book.name