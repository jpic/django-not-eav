import importlib

from django.db import models
from django.db.models import signals
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType

from south.db import db
from south.v2 import SchemaMigration


KIND_CHOICES = (
    ('django.db.models.fields.IntegerField', _('integer')),
    ('django.db.models.fields.FloatField', _('decimal number')),
    ('django.db.models.fields.CharField', _('short text')),
    ('django.db.models.fields.TextField', _('text')),
    ('django.db.models.fields.DateTimeField', _('date and time')),
    ('django.db.models.fields.DateField', _('date only')),
    ('django.db.models.fields.TimeField', _('time only')),
    ('django.db.models.fields.ImageField', _('image')),
    ('django.db.models.fields.FileField', _('file')),
)


class Attribute(models.Model):
    content_type = models.ForeignKey(ContentType)
    name = models.CharField(max_length=100)

    verbose_name = models.CharField(max_length=100, null=True, blank=True)
    help_text = models.TextField(blank=True)
    kind = models.CharField(max_length=70, choices=KIND_CHOICES)

    @classmethod
    def factory(cls, model, **kwargs):
        return Attribute(
            content_type=ContentType.objects.get_for_model(model), **kwargs)

    @property
    def field_instance(self):
        bits = self.kind.split('.')
        module = importlib.import_module('.'.join(bits[:-1]))
        field_class = getattr(module, bits[-1])
        return field_class(**self.field_kwargs)

    @property
    def field_kwargs(self):
        kwargs = dict(null=True, blank=True, verbose_name=self.verbose_name,
            help_text=self.help_text)

        if self.kind == 'django.db.models.fields.FileField':
            kwargs['upload_to'] = 'custom_filefields'
        elif self.kind == 'django.db.models.fields.ImageField':
            kwargs['upload_to'] = 'custom_imagefields'
        elif self.kind == 'django.db.models.fields.CharField':
            kwargs['max_length'] = 255

        return kwargs

    def create_column(self):
        sm = SchemaMigration()
        db.add_column(self.content_type.model_class()._meta.db_table,
            self.name, sm.gf(str(self.kind))(**self.field_kwargs))

    def delete_column(self):
        db.delete_column(self.content_type.model_class()._meta.db_table,
            self.name)

    def contribute_to_class(self):
        self.field_instance.contribute_to_class(
            self.content_type.model_class(), self.name)


def create_attribute(sender, instance, created, **kwargs):
    from django.contrib import admin
    admin.autodiscover()

    if not created:
        return

    instance.create_column()
    instance.contribute_to_class()
signals.post_save.connect(create_attribute, sender=Attribute)


def delete_attribute(sender, instance, **kwargs):
    instance.delete_column()
signals.pre_delete.connect(delete_attribute, sender=Attribute)
