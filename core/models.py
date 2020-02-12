from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        abstract = True

