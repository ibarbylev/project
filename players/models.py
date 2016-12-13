from django.db import models


class Exercises (models.Model):
    kod_exercise = models.CharField(max_length=15)
    name_exercise = models.CharField(max_length=50)
    video_exercise = models.URLField(max_length=150,
                                     blank=True,
                                     null=True)
    audio_exercise = models.URLField(max_length=150,
                                     blank=True,
                                     null=True)
    question = models.TextField(default='')
    answers = models.TextField(default='')
    true_answer = models.TextField(default='')
    audio_true_answer = models.URLField(max_length=150,
                                        blank=True,
                                        null=True)
    permission = models.CharField(max_length=10)
    estimated_time = models.DecimalField(max_digits=10, decimal_places=3) # время в часах, как десятичная дробь
    limited_time  = models.DecimalField(max_digits=10, decimal_places=3) # время в часах, как десятичная дробь


    def __str__(self):
        return self.kod_exercise
