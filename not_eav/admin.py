from django.contrib import admin

from forms import AttributeFormBase, AttributeEditForm
from models import Attribute


class AttributeAdmin(admin.ModelAdmin):
    list_filter = ('content_type', 'kind')
    list_display = ('content_type', 'name', 'kind', 'verbose_name')

    form = AttributeFormBase

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return AttributeEditForm.Meta.exclude
        else:
            return []

admin.site.register(Attribute, AttributeAdmin)
