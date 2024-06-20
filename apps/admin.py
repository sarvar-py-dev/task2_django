from django.contrib import admin

from apps.models import Card


@admin.register(Card)
class CardModelAdmin(admin.ModelAdmin):
    pass
