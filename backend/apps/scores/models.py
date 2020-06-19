from django.db import models

from apps.users.models import User


class Score(models.Model):
    count = models.SmallIntegerField(
        verbose_name='Score counts',
        default=0)

    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True)

    class Meta:
        verbose_name = 'Score'
        verbose_name_plural = 'Scores'
