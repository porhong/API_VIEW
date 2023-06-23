from django.db import models
from datetime import date

class Movie(models.Model):
    title = models.CharField(max_length=500)
    release_date = models.DateField(default=date.today())
    def __str__(self):
        return self.title
    class Meta:
        db_table = "movie"