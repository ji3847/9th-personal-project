
from django.db import models
from django.utils import timezone

# Create your models here.

class HashTag(models.Model):
    hashtag_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.hashtag_name

class Movielog(models.Model):
    title=models.CharField(max_length=200)
    director= models.CharField(max_length=100)
    release_day= models.CharField(max_length=100)
    body=models.TextField()
    pub_date=models.DateTimeField('date published')
    hashtag = models.ManyToManyField(HashTag)
    #image=models.ImageField(upload_to='images/',blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Comment(models.Model):
    post = models.ForeignKey(Movielog, related_name='comments', on_delete=models.CASCADE)
    author_name = models.CharField(max_length=20)
    comment_text = models.TextField()
    created_at = models.DateTimeField(default= timezone.now)

    def apporve(self):
        self.save()

    def __str__(self):
        return self.comment_text




