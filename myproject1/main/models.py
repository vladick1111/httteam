from django.db import models


class Vacancy(models.Model):
    name = models.CharField(max_length=40, blank=False)
    descrip = models.TextField()
    responses = models.IntegerField()


class Candidate(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    second_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    vacancy = models.CharField(max_length=40, blank=False)


class Worker(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    second_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    vacancy = models.CharField(max_length=40, blank=False)
    date_birth = models.DateField()
    competence = models.TextField()
    work_experience = models.IntegerField()
