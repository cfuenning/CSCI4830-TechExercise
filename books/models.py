from django.db import models #imports ORM module

#defines table named score 
#uses models.Model which is base class for all Django models
class Score(models.Model): 

    #each attribute represents field in table
    name = models.CharField(max_length=100)
    value = models.IntegerField() 
    
    def __str__(self): 
        return self.name
