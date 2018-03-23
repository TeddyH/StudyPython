# blog/models.py

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey("auth.User")
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now
    )
    pulblished_date = models.DateTimeField(    # 글 노출 여부
        blank=True, null=True
    )

    def publish(self):
         self.published_date = timezone.now()
         self.save()

    def __str__(self):  # _언더스코어가 2개입니다.
        return self.title