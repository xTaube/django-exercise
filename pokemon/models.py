from django.db import models
from django.conf import settings

def upload_status_image(instance, filename):
    return "pokemon/{user}/{filename}".format(user=instance.user, filename=filename)

class PokemonQuerySet(models.QuerySet):
    pass

class PokemonManager(models.Manager):
    def get_queryset(self):
        return PokemonQuerySet(self.model, using=self._db)


class Pokemon(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_status_image, null=True, blank=True)
    updates = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    object = PokemonManager()

    def __str__(self):
        return str(self.content)[:50]

