from django.db import models

from apps.common.models import BaseModel
from ckeditor.fields import RichTextField


class MovieNews(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='movie_news', null=True, blank=True)
    premiere_date = models.DateField(null=True, blank=True)
    trailer = models.URLField(unique=True, null=True, blank=True)
    views = models.IntegerField(default=0, null=True, blank=True)
    ganres = models.ManyToManyField("common.Genre", blank=True)
    regisseurs = models.ManyToManyField(
        'common.Actor',
        blank=True,
        limit_choices_to={"type": 1},
        related_name='newsregisseurs',
        )
    category = models.ForeignKey(
        'common.Category',
        on_delete=models.CASCADE,
        related_name='movienews',
        related_query_name='moviesnews',
        null=True, blank=True,
        limit_choices_to={"status": 1},
    )
    country = models.ForeignKey("common.Country", on_delete=models.CASCADE, null=True, blank=True)
    actor = models.ManyToManyField(
        "common.Actor",
        blank=True,
        limit_choices_to={"type": 0},
        related_name="newsactors",
        )

    def __str__(self):
        return self.name
