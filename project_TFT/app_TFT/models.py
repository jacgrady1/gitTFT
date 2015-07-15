from django.db import models

# Create your models here.

class Course(models.Model):
    #user = models.ForeignKey(User)
    id= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    brief = models.CharField(max_length=200,blank=True)
    description = models.CharField(max_length=1000,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='photos/course_photos')
    start_date = models.DateField(blank=True)
    start_time = models.TimeField(blank=True)
    price = models.FloatField(blank=True)

    def __unicode__(self):
         return self.name



