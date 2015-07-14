from django.db import models

# Create your models here.

class Course(models.Model):
    #user = models.ForeignKey(User)
    id= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='photos/course_photos')
    start_date = models.DateField()
    start_time = models.TimeField(null=True)
    price = models.FloatField()

    def __unicode__(self):
         return self.name



