from django.core.validators import RegexValidator
from django.db import models


class Position(models.Model):
    job_title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.job_title


class Employee(models.Model):
    name_regex = RegexValidator(regex=r'^[а-яА-Яa-zA-Z]+$', message="ФИО должно содержать только буквы.")
    last_name = models.CharField(max_length=100, validators=[name_regex])
    first_name = models.CharField(max_length=100, validators=[name_regex])
    middle_name = models.CharField(max_length=100, validators=[name_regex])
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    invite_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
