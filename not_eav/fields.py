import re

from django.utils.translation import ugettext_lazy as _
from django import forms
from django.db import models


class NameFormField(forms.CharField):
    NAME_REGEXP = r'^[a-z][a-z\d_]+$'

    def validate(self, value):
        super(NameFormField, self).validate(value)

        if re.match(self.NAME_REGEXP, value) is None:
            raise forms.ValidationError(_(u'Attribute name should only'
                'contain alphanumeric characters and underscore'))


class NameField(models.CharField):
    def formfield(self, **kwargs):
        kwargs['max_length'] = self.max_length
        kwargs['form_class'] = NameFormField
        return super(NameField, self).formfield(**kwargs)
