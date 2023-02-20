from django.db import models

BROWNIAN_MOTION_CHOICES = (
    ('bm','Brownian Motion'),
    ('gbm', 'Geometric Brownian Motion')
)

class Graph(models.Model):
    mu = models.DecimalField(decimal_places=3, max_digits=10)
    sigma = models.DecimalField(decimal_places=3, max_digits=10)
    s_0 = models.DecimalField(decimal_places=3, max_digits=10)
    t = models.DecimalField(decimal_places=3, max_digits=10)
    n = models.DecimalField(decimal_places=3, max_digits=10)
    no_of_paths = models.IntegerField()
    choice = models.CharField(max_length=6, choices=BROWNIAN_MOTION_CHOICES, default='bm')