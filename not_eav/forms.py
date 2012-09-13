from django import forms

from models import BaseFieldModel


class BaseFieldModelEditForm(forms.ModelForm):
    class Meta:
        exclude = ('content_type', 'name', 'required')
        model = BaseFieldModel
