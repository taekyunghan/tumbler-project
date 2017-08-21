from django.db import models


class Eco(models.Model):
    ecouser = models.ForeignKey('auth.User')
    ecocount = models.IntegerField(default=1)
    ecotime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.ecouser)

