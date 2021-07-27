from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

class Batch(models.Model):
    name = models.CharField(max_length=30)
    style = models.CharField(max_length=30)
    volume = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    start_date = models.DateField('brewed', auto_now_add=True)
    end_date = models.DateField('finished', blank=True)
    score = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)], blank=True)
    comment = models.CharField(max_length=255, blank=True)
    class Meta:
        # a list of batches will return the newest first
        ordering = ['-start_date']
