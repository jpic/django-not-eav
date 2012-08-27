import re

from django.utils.translation import ugettext_lazy as _
from django import forms

from models import Attribute

NAME_REGEXP = r'^[a-z][a-z\d_]+$'


class AttributeFormBase(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data['name']

        if re.match(NAME_REGEXP, name) is None:
            raise forms.ValidationError(_(u'Attribute name should only'
                'contain alphanumeric characters and underscore'))
        return name

    class Meta:
        model = Attribute


class AttributeCreateForm(AttributeFormBase):
    pass


class AttributeEditForm(AttributeFormBase):
    class Meta:
        exclude = ('content_type', 'name', 'kind')
