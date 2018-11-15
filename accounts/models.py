from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from projects.models import Language, Framework


class Profile(models.Model):
    USER_TYPE_CHOICES = (
        ('recruiter', 'Recruiter'),
        ('developer', 'Developer'),
    )
    STAGE_CHOICES = (
        ('recruiter_filling_details', 'recruiter_filling_details'),
        ('developer_filling_details', 'developer_filling_details'),
        ('complete', 'complete'),
    )
    YEARS_ACTIVE_CHOICES = (
        ('1-2', '1-2'),
        ('2-4', '2-4'),
        ('4-above', '4-above'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_type = models.CharField(choices=USER_TYPE_CHOICES, null=True, blank=True, max_length=30, default='developer')
    stage = models.CharField(choices=STAGE_CHOICES, default='developer_filling_details', max_length=100)
    profile_photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    phone_number = models.CharField(max_length=140, null=True, blank=True)
    # developer profile
    github_repo = models.URLField(blank=True, null=True, )
    language = models.ForeignKey(Language, on_delete=models.SET_NULL,
                                 related_name='languages', null=True, blank=True)
    framework = models.ForeignKey(Framework, on_delete=models.DO_NOTHING, related_name='frameworks', null=True,
                                  blank=True)
    years = models.CharField(max_length=30, choices=YEARS_ACTIVE_CHOICES, null=True, blank=True)
    # recruiter profile
    company = models.CharField(max_length=140, null=True, blank=True)
    job_role = models.CharField(max_length=140, null=True, blank=True)
    industry = models.CharField(max_length=80, null=True, blank=True)
    staff_size = models.IntegerField(null=True, blank=True)
    company_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    def photo(self, default_path="default_user_photo.png"):
        if self.profile_photo:
            return self.profile_photo
        return default_path

    def get_absolute_url(self):
        return '/accounts/profile/'

    @property
    def full_name(self):
        return self.user.get_full_name()

    @property
    def date_joined(self):
        return self.user.date_joined

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
