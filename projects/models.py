from django.contrib.auth.models import User
from django.db import models


# Create your models here.

# TODO: add model for category to classify all projects using project category, can be multiple ie frontend, backend
# TODO: categorise language into frontend, backend etc


class Language(models.Model):
    name = models.CharField(max_length=140)

    def __str__(self):
        return self.name


class Framework(models.Model):
    name = models.CharField(max_length=140)
    language = models.ForeignKey(Language, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Devtype(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Projecttype(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=140)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True, null=True, )
    level = models.CharField(max_length=200, blank=True, null=True, )
    concept = models.CharField(max_length=200, blank=True, null=True, )
    projectimage1 = models.CharField(max_length=200, blank=True, null=True, )
    projectimage2 = models.CharField(max_length=200, blank=True, null=True, )
    projectimage3 = models.CharField(max_length=200, blank=True, null=True, )
    requirement1 = models.CharField(max_length=200, blank=True, null=True, )
    requirement2 = models.CharField(max_length=200, blank=True, null=True, )
    requirement3 = models.CharField(max_length=200, blank=True, null=True, )
    requirement4 = models.CharField(max_length=200, blank=True, null=True, )
    requirement5 = models.CharField(max_length=200, blank=True, null=True, )
    framework = models.ForeignKey(Framework, on_delete=False, null=True)
    devtype = models.ForeignKey(Devtype, on_delete=False, null=True)
    projecttype = models.ForeignKey(Projecttype, on_delete=False, null=True)

    def __str__(self):
        return self.name


class OngoingProjects(models.Model):
    assigner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigner')
    candidate = models.ForeignKey(User, on_delete=models.CASCADE, related_name='candidate')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # TODO bad code, improve by actually fixing circular imports
    # correct: transaction = models.ForeignKey(Transaction, null=True, blank=True)
    transaction = models.CharField(max_length=140, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
