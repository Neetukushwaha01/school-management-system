from django.db import models

# Create your models here.
from django.db import models


class School( models.Model ):
    name = models.CharField( max_length=100 )
    email = models.EmailField( unique=True )
    city = models.CharField( max_length=50 )
    pin_code = models.CharField( max_length=6 )
    password = models.CharField( max_length=128 )


class Student( models.Model ):
    GRADE_CHOICES = (
        (1, 'First'),
        (2, 'Second'),
        (3, 'Third'),
        (4, 'Fourth'),
        (5, 'Fifth'),
        (6, 'Sixth'),
        (7, 'Seventh'),
        (8, 'Eighth'),
        (9, 'Ninth'),
        (10, 'Tenth'),
        (11, 'Eleventh'),
        (12, 'Twelfth'),
    )
    name = models.CharField( max_length=100, blank=True )
    username = models.CharField( max_length=100, unique=True )
    password = models.CharField( max_length=128 )
    grade = models.IntegerField( choices=GRADE_CHOICES )
    school = models.ForeignKey( School, on_delete=models.CASCADE )
