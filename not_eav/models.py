import importlib

from django.db import models
from django.db.models import signals
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType

from model_utils.managers import InheritanceManager
from south.db import db
from south.v2 import SchemaMigration

from fields import NameField

KIND_CHOICES = (
    ('django.db.models.fields.IntegerField', _('integer')),
    ('django.db.models.fields.FloatField', _('decimal number')),
    ('django.db.models.fields.CharField', _('short text')),
    ('django.db.models.fields.TextField', _('text')),
    ('django.db.models.fields.DateTimeField', _('date and time')),
    ('django.db.models.fields.DateField', _('date only')),
    ('django.db.models.fields.TimeField', _('time only')),
    ('django.db.models.fields.files.ImageField', _('image')),
    ('django.db.models.fields.files.FileField', _('file')),
)


class BaseFieldModel(models.Model):
    content_type = models.ForeignKey(ContentType)
    name = NameField(max_length=200,
            help_text=_(u'Short name with only underscores and letters and '
                'numbers, must start with a letter'))
    verbose_name = models.CharField(max_length=100, null=True, blank=True)
    help_text = models.TextField(blank=True)
    required = models.BooleanField()
    default = models.TextField(blank=True, null=True)

    objects = InheritanceManager()

    class Meta:
        app_label = 'not_eav'

    def field_instance(self):
        bits = self.module_class.split('.')
        module = importlib.import_module('.'.join(bits[:-1]))
        field_class = getattr(module, bits[-1])
        return field_class(**self.field_kwargs())

    def field_kwargs(self):
        kwargs = {}
        if self.required:
            kwargs['null'] = False
            kwargs['blank'] = False
        else:
            kwargs['null'] = True
            kwargs['blank'] = True

        kwargs['default'] = self.default

        if self.verbose_name:
            kwargs['verbose_name'] = self.verbose_name

        if self.help_text:
            kwargs['help_text'] = self.help_text

        if self.module_class == 'django.db.models.fields.FileField':
            kwargs['upload_to'] = 'not_eav_filefields'
        elif self.module_class == 'django.db.models.fields.ImageField':
            kwargs['upload_to'] = 'not_eav_imagefields'

        return kwargs

    def create_column(self):
        sm = SchemaMigration()
        db.add_column(self.content_type.model_class()._meta.db_table,
            self.name, sm.gf(str(self.module_class))(**self.field_kwargs()))

    def delete_column(self):
        db.delete_column(self.content_type.model_class()._meta.db_table,
            self.name)

    def contribute_to_class(self):
        self.field_instance().contribute_to_class(
            self.content_type.model_class(), self.name)

    def remove_from_class(self):
        model_class = self.content_type.model_class()

        model_class._meta.local_fields[:] = [
            x for x in model_class._meta.local_fields if x.name != self.name]
        model_class._meta.fields[:] = [
            x for x in model_class._meta.fields if x.name != self.name]

        if hasattr(model_class._meta, '_field_cache'):
            del model_class._meta._field_cache


def create_attribute(sender, instance, created, **kwargs):
    if not isinstance(instance, BaseFieldModel):
        return

    from django.contrib import admin
    admin.autodiscover()

    if not created:
        return

    instance.create_column()
    instance.contribute_to_class()
signals.post_save.connect(create_attribute)


def delete_attribute(sender, instance, **kwargs):
    if not isinstance(instance, BaseFieldModel):
        return

    instance.remove_from_class()
    instance.delete_column()

    from django.contrib import admin
    admin.autodiscover()
signals.pre_delete.connect(delete_attribute)
