from django.db import models

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    roll_number = models.CharField(max_length=20, unique=True)
    admission_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.roll_number})"

