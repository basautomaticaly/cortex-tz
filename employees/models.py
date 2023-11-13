from django.db import models


class Position(models.Model):
    job_title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.job_title


class Employee(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    invite_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
