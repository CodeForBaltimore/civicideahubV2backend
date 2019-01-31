from django.db import models

# Create your models here.
class Idea(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    problem = models.CharField(max_length=500, blank=True, unique=False)
    potential_solution = models.CharField(max_length=500, blank=True, unique=False)
    likeCount = models.IntegerField(default=0)
    coderCount = models.IntegerField(default=0)
    imageURL = models.CharField(max_length=255, blank=True, unique=False)
    owner = models.ForeignKey('auth.User', 
                                related_name = 'ideas', 
                                on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)
