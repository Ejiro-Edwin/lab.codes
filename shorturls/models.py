import random
import string

from django.db import models


class ShortURL(models.Model):

    original = models.URLField(max_length=500)
    shortened_slug = models.CharField(max_length=6, blank=True)

    clicks = models.IntegerField(default=0)

    def increment_clicks(self):
        self.clicks += 1
        self.save()

    def __str__(self):
        return f'http://lab.codes/{self.shortened_slug} -> {self.original}'

    def save(self, *args, **kwargs):
        if not self.pk:
            if not self.shortened_slug:
                self.shortened_slug = ''.join(random.sample(string.ascii_lowercase + string.digits, 6))

        super(ShortURL, self).save(*args, **kwargs)
