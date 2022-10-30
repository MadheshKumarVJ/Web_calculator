from random import choices
from django.apps import AppConfig
from django import forms


class CalcConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "calc"
