from django.db import models


# Create your models here.
class Articles(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=60, db_index=True)
    paragraph = models.TextField(blank=True, db_index=True)
    body = models.TextField(blank=True, db_index=True)
    image = models.CharField(max_length=60, blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.title)


class Properties(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=60, db_index=True)
    body = models.TextField(blank=True, db_index=True)
    image = models.CharField(max_length=60, blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.title)

class Reviews(models.Model):
    id = models.BigIntegerField(primary_key=True)
    author = models.CharField(max_length=60, db_index=True)
    text = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.author)