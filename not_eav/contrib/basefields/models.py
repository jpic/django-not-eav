from django.db import models
from django.utils.translation import ugettext_lazy as _

from not_eav.models import BaseFieldModel


class BooleanFieldModel(BaseFieldModel):
    module_class = 'django.db.models.fields.BooleanField'

    class Meta:
        verbose_name = _(u'Yes/No field')


class CharFieldModel(BaseFieldModel):
    module_class = 'django.db.models.fields.CharField'
    max_length = models.PositiveIntegerField()
    max_length.not_changeable = True

    def field_kwargs(self):
        kwargs = super(CharFieldModel, self).field_kwargs()
        kwargs['max_length'] = self.max_length
        return kwargs

    class Meta:
        verbose_name = _(u'One-line text field')


class DateFieldModel(BaseFieldModel):
    module_class = 'django.db.models.fields.DateField'

    class Meta:
        verbose_name = _(u'Date field')


class DateTimeFieldModel(BaseFieldModel):
    module_class = 'django.db.models.fields.DateTimeField'

    class Meta:
        verbose_name = _(u'Date and time field')


class DecimalFieldModel(BaseFieldModel):
    module_class = 'django.db.models.fields.DecimalField'

    class Meta:
        verbose_name = _(u'Decimal number field')


class EmailFieldModel(BaseFieldModel):
    module_class = 'django.db.models.fields.EmailField'

    class Meta:
        verbose_name = _(u'Email field')


class IntegerFieldModel(BaseFieldModel):
    module_class = 'django.db.models.fields.IntegerField'

    class Meta:
        verbose_name = _(u'Integer field')


class IPAddressFieldModel(BaseFieldModel):
    module_class = 'django.db.models.fields.IPAddressField'

    class Meta:
        verbose_name = _(u'IP Address field')


class NullBooleanFieldModel(BaseFieldModel):
    module_class = 'django.db.models.fields.NullBooleanField'

    class Meta:
        verbose_name = _(u'Yes/No/Maybe field')


class PositiveIntegerFieldModel(BaseFieldModel):
    module_class = 'django.db.models.fields.PositiveIntegerField'

    class Meta:
        verbose_name = _(u'Positive integer field')


class TextFieldModel(BaseFieldModel):
    module_class = 'django.db.models.fields.TextField'

    class Meta:
        verbose_name = _(u'Multiline text field')


class TimeFieldModel(BaseFieldModel):
    module_class = 'django.db.models.fields.TimeField'

    class Meta:
        verbose_name = _(u'Time field')


class URLFieldModel(BaseFieldModel):
    module_class = 'django.db.models.fields.URLField'

    class Meta:
        verbose_name = _(u'URL field')
