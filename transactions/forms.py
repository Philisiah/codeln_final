from django import forms
from django.forms import ModelForm, Form

from projects.models import Language, Framework
from transactions.models import Candidate


class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        exclude = ('transaction',)


def language_choices():
    return tuple([(language.name, language.name)
                  for language in Language.objects.all()])


def framework_choices():
    return tuple([(framework.name, framework.name)
                  for framework in Framework.objects.all()])


class StackForm(forms.Form):
    language = forms.ChoiceField(choices=language_choices, widget=forms.RadioSelect())
    framework = forms.ChoiceField(choices=framework_choices, widget=forms.RadioSelect())


class SourcingForm(Form):
    job_roles = (
        ('Full Stack Developer', 'Full Stack Developer'),
        ('Frontend Developer', 'Frontend Developer'),
        ('Backend  Developer', 'Backend  Developer'),
        ('Android Developer', 'Android  Developer'),
        (' Graphic Designer', 'Graphic Designer'),
        ('IOS  Developer', 'IOS Developer'),
        ('Data Scientist', 'Data Scientist'),
    )
    engagement = (
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Contract', 'Contract'),
        ('Freelance', 'Freelance'),
    )
    yes_no = (
        ('yes', 'yes'),
        ('no', 'no'),
    )
    email_address = forms.EmailField(required=True)
    phone_number = forms.IntegerField()
    name = forms.CharField(max_length=255)
    company_name = forms.CharField(max_length=255)
    job_role = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=job_roles)
    engagement_types = forms.ChoiceField(choices=engagement)
    tech_stack = forms.CharField(max_length=255)
    project_description = forms.CharField(widget=forms.Textarea)
    Number_of_devs_needed = forms.IntegerField()
    renumeration_in_dollars = forms.IntegerField()
    tech_staff = forms.ChoiceField(choices=yes_no)
    skills_test = forms.ChoiceField(choices=yes_no)
