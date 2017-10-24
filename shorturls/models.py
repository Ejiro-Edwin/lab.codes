import random
import string

from django.db import models
from django.core.exceptions import ValidationError


class ShortURL(models.Model):

    original = models.URLField(max_length=500)
    shortened_slug = models.CharField(max_length=25, blank=True, unique=True)

    clicks = models.IntegerField(default=0)

    def increment_clicks(self):
        self.clicks += 1
        self.save()

    def clean(self):
        if self.shortened_slug == 'admin':
            raise ValidationError('Slug "admin" cannot be created')

    def __str__(self):
        return f'http://lab.codes/{self.shortened_slug} -> {self.original}'

    def save(self, *args, **kwargs):
        self.clean()
        if not self.pk:
            if not self.shortened_slug:
                self.shortened_slug = ''.join(random.sample(string.ascii_lowercase + string.digits, 6))

        super(ShortURL, self).save(*args, **kwargs)
