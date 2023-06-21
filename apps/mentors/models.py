# from django.contrib.auth.models import User
from django.db import models
from static.image import *
from apps.users.models import User


class Skills(models.Model):
    text = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class Employment(models.Model):
    weekday = models.CharField(max_length=20)
    weekend = models.CharField(max_length=20)

    def __str__(self):
        return f'Weekday: {self.weekday}' \
               f'Weekend: {self.weekend}'


class Mentor(models.Model):
    DIRECTION_CHOICES = (
        ('Backend', 'Backend'),
        ('Frontend', 'Frontend'),
        ('UX/UI', 'UX/UI'),
        ('Android', 'Android'),
        ('IOS', 'IOS')
    )

    MONTH_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7')
    )

    is_active = models.BooleanField(default=False, blank=True)
    image = models.ImageField(blank=True, upload_to='mentors/', default='mentors/default.jpg')
    direction = models.CharField(choices=DIRECTION_CHOICES, max_length=10)
    month = models.CharField(max_length=5, choices=MONTH_CHOICES)
    group = models.CharField(max_length=20)
    name = models.CharField(max_length=15)
    about_me = models.TextField()
    contact = models.URLField()
    skills = models.ManyToManyField(Skills)
    employment = models.ForeignKey(Employment, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Mentor'
        verbose_name_plural = 'Mentors'

    def __str__(self):
        return f'{self.name}'





