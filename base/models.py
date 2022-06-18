from django.db import models


class Msg(models.Model):
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.pk)
