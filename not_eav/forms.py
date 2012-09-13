from django import forms

from models import Attribute


class AttributeEditForm(forms.ModelForm):
    class Meta:
        exclude = ('content_type', 'name', 'kind')
        model = Attribute
