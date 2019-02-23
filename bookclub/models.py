from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    poster = models.CharField(max_length=300,default='')
    author = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    synopsis = models.TextField()
    published_year = models.CharField(max_length=4)
    book_cover = models.ImageField(upload_to='image',default = '/none/no-img.jpg')
    submitted_date = models.DateTimeField(default=timezone.now)
    ratings = models.FloatField(default=0.0)
    isbn_number = models.IntegerField(default=0)


    def publish(self):
        #self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('bookclub.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    review_title = models.CharField(max_length=200,default = '')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
