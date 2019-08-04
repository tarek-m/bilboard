from django.db import models

# Create your models here.

class Post (models.Model):

    post_title= models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    post_content= models.TextField()
    post_author = models.CharField(max_length=100)




