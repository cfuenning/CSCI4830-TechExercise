from django.db import models #imports ORM module
from django.core.validators import MinValueValidator, MaxValueValidator

#defines table named Bookshelf 
#uses models.Model which is base class for all Django models
class Bookshelf(models.Model): 

    genre_choices = [
        ('FIC', 'Fiction'),
        ('NF', 'Non-Fiction'),
        ('SCI', 'Science Fiction'),
        ('FAN', 'Fantasy'),
        ('MYS', 'Mystery'),
        ('HOR', 'Horror/Thriller'),
        ('ROM', 'Romance'),
        ('AAA', 'Action & Adventure'),
    ]

    #each attribute represents column in table
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=3, choices=genre_choices, default='FIC')
    note = models.CharField(max_length=500, blank=True, null=True) #allows empty entry in forms & database
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(11)]) 
    
    def __str__(self): 
        return self.name
