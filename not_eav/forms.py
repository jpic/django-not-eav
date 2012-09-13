from django import forms

from models import Attribute


class AttributeFormBase(forms.ModelForm):
    class Meta:
        model = Attribute


class AttributeCreateForm(AttributeFormBase):
    pass


class AttributeEditForm(AttributeFormBase):
    class Meta:
        exclude = ('content_type', 'name', 'kind')
