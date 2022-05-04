from django.db import models

class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    course_title = models.CharField(max_length=100)
    course_description = models.CharField(max_length=250)
    credits = models.IntegerField()
    instructor = models.CharField(max_length=50)
    start_date = models.DateField()
