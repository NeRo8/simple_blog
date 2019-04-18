from django.db import models
from django.utils import timezone
# Create your models here.


class Articles(models.Model):
    title = models.CharField(max_length=120)
    textArticle = models.TextField()
    datePub = models.DateTimeField(default=timezone.now)
    likeIt = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
