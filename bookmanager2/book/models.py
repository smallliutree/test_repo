from django.db import models

# Create your models here.
class BookInfo(models.Model):
    name = models.CharField(max_length=10, verbose_name='书籍名称')
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'
        verbose_name = '图书'

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    GENDER_CHOICE = (
        (0, 'male'),
        (1, 'female')
    )
    name = models.CharField(max_length=10)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=0)
    description = models.CharField(max_length=100)
    is_delete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    class Meta:
        db_table = 'peopleinfo'

    def __str__(self):
        return self.name