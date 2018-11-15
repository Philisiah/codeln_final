from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from taggit.managers import TaggableManager


# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=140)

    def __str__(self):
        return self.name


class Framework(models.Model):
    name = models.CharField(max_length=140)
    language = models.ForeignKey(Language, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class DevType(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('projects:dev-type', args=(self.slug,))

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)


class ProjectLevel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProjectType(models.Model):
    name = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('projects:project-type', args=(self.slug,))

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=140)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    level = models.ForeignKey(ProjectLevel, null=True, blank=True, on_delete=models.CASCADE)
    concepts = TaggableManager(blank=True)
    project_images = models.CharField(max_length=200, blank=True, null=True, )
    requirements = models.CharField(max_length=200, blank=True, null=True, )
    devtype = models.ForeignKey(DevType, on_delete=False, null=True, blank=True)
    projecttype = models.ForeignKey(ProjectType, on_delete=False, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)


class RecruiterProject(models.Model):
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    framework = models.ForeignKey(Framework, on_delete=False, null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=False, null=True, blank=True)


class OngoingProjects(models.Model):
    assigner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigner')
    candidate = models.ForeignKey(User, on_delete=models.CASCADE, related_name='candidate')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # TODO bad code, improve by actually fixing circular imports
    # correct: transaction = models.ForeignKey(Transaction, null=True, blank=True)
    transaction = models.CharField(max_length=140, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
