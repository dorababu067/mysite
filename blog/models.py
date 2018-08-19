from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
  
STATUS_CHOICE =(
    ('draft','Draft'),
    ('publish','published')     
)

class Post(models.Model):
    title        =  models.CharField(max_length=256)
    authour      =  models.ForeignKey(User,on_delete=models.CASCADE)
    likes        =  models.ManyToManyField(User,related_name = "likes",blank=True)
    content      =  models.TextField()
    created      =  models.DateField(auto_now_add=True)
    updated      =  models.DateField(auto_now=True)
    status       =  models.CharField(max_length=10,choices=STATUS_CHOICE,default='draft')

    def __str__(self):
        return "{}--{}".format(self.title,self.authour)
    
    def get_absolute_url(self):
        return reverse('details',kwargs={'id':self.pk})

    def likes_count(self):
        return self.likes.count()

class Comments(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return "{}--by {}".format(self.comment,self.user.username)

class Profile(models.Model):
    user    =   models.OneToOneField(User,on_delete = models.CASCADE)
    profile_pic = models.ImageField(upload_to='images',null=True,blank=True)
    DOB         = models.DateField(null=True)
    qualification = models.CharField(max_length=256,null=True)
    Bio         = models.TextField(null=True)

    def __str__(self):
        return self.user.username

