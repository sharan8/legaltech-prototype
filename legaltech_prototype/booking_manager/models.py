from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    lawyer = models.CharField(max_length=100)

    def address_slug(self):
        return slugify(self.address)

    def children(self):
        return Session.objects.filter(location=self)

class Session(models.Model):
    DAY_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday')
    )

    STATUS_CHOICES = (
        ('Available', 'Available'),
        ('Booked', 'Booked'),
    )

    day = models.CharField(default='Monday', max_length=15, choices=DAY_CHOICES)
    start_time = models.TimeField(default=0000)
    end_time = models.TimeField(default=0000)
    status = models.CharField(default='Available', max_length=15, choices=STATUS_CHOICES)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
