import uuid

from django.db import models


class Movie(models.Model):
    lookup_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        db_index=True,
    )
    order = models.IntegerField(
        blank=False,
        default=100_000,
    )
    poster = models.ImageField(upload_to='poster')
    name = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'movie'
        ordering = ('order',)

    def __str__(self):
        return str(self.lookup_id)
