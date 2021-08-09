from aldryn_apphooks_config.models import AppHookConfig
from aldryn_apphooks_config.utils import setup_config
from app_data import AppDataForm
from django.db import models
from django import forms
from django.utils.translation import gettext_lazy as _


class NewsConfig(AppHookConfig):
    paginate_by = models.PositiveIntegerField(
        _('Paginate size'),
        blank=False,
        default=5,
    )
    namespace = models.CharField(
        _('Instance namespace'),
        default=None,
        max_length=100,
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        self.pk = 1
        self.namespace = 'news'
        super().save(*args, **kwargs)

setup_config(NewsConfig, NewsConfig)
