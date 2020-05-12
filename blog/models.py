from django.db import models
from django.utils import timezone

# import a user model,
from django.contrib.auth.models import User


# user model and posts model have a on - many relation
# user has many posts - but a post belong to one user
# Create your models here.

class Posts(models.Model):
    title = models.CharField("title", max_length=100)
    content = models.TextField("content", max_length=200)
    date = models.DateTimeField(default=timezone.now)
    # set author as foreign key - relate to User model
    # set on_delete to cascade sicne a author is deletd -all his posts should be removed
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
