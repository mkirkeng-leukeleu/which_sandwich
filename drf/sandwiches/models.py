from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField

class Sandwiches(Page):
    pass

class Sandwich(Page):
    name = models.CharField(max_length=250)
    short_description = models.CharField(max_length=250)
    vegetarian = models.BooleanField(blank=True)
    long_description = RichTextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL
    )

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('short_description'),
        FieldPanel('vegetarian'),
        FieldPanel('long_description'),
        FieldPanel('image'),
    ]

    api_fields = [
        APIField('name'),
        APIField('short_description'),
        APIField('vegetarian'),
        APIField('long_description'),
        APIField('image', serializer=ImageRenditionField('max-800x800')),
    ]
