from django.db import models

# Create your models here.


class Problem(models.Model):
    name = models.CharField(max_length=100)
    coa = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    booking_manager = models.BooleanField(default=False)

    def children(self):
        return Problem.objects.filter(parent=self)
