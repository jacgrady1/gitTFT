from django.db import models
from django.core.validators import URLValidator
# Create your models here.

class Course(models.Model):
    #user = models.ForeignKey(User)
    id= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=50)
    brief = models.CharField(max_length=200,blank=True)
    description = models.CharField(max_length=1000,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='photos/course_photos')
    start_date = models.DateField(blank=True)
    start_time = models.TimeField(blank=True)
    price = models.FloatField(blank=True)
    group_price = models.FloatField(blank=True)
    promotion_info= models.CharField(blank=True,max_length=200)

    def __unicode__(self):
         return self.name


class Question(models.Model):
    content = models.CharField(max_length=300)
    answer = models.CharField(max_length=2000,blank=True)
    course = models.ForeignKey(Course)

    def __unicode__(self):
         return self.content

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    course = models.ManyToManyField(Course)
    school = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    picture = models.ImageField(upload_to='photos/teacher_photos',blank=True)

    LECTURER = 'Lecturer'
    COACH = 'Coach'

    ROLE_CHOICES = (
        (LECTURER, 'Lecturer'),
        (COACH, 'Coach'),
    )
    role = models.CharField(max_length=10,choices=ROLE_CHOICES,default=LECTURER)

    def __unicode__(self):
        return self.name

class Lecture(models.Model):
    course = models.ForeignKey(Course)
    num = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Chapter(models.Model):
    lecture = models.ForeignKey(Lecture)
    content = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.content


class Hashtag(models.Model):
    course = models.ForeignKey(Course)
    name = models.CharField(max_length=100)
    url = models.TextField(validators=[URLValidator()])

    def __unicode__(self):
        return self.url

