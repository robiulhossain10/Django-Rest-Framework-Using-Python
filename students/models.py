from django.db import models

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100,default="Unknown")
    mothers_name = models.CharField(max_length=100,default="Unknown")
    email = models.EmailField(unique=True)
    roll_number = models.CharField(max_length=20, unique=True)
    admission_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.roll_number}) {self.admission_date} {self.email} {self.fathers_name} {self.mothers_name}"

