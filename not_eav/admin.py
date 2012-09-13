from django.contrib import admin

from forms import BaseFieldModelEditForm
from models import BaseFieldModel


class BaseFieldModelAdmin(admin.ModelAdmin):
    list_filter = ('content_type',)
    list_display = ('content_type', 'name', 'verbose_name')

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            exclude = list(BaseFieldModelEditForm.Meta.exclude)

            for field in obj._meta.fields:
                not_changeable = getattr(field, 'not_changeable', False)
                if not_changeable:
                    exclude.append(field.name)
        else:
            exclude = []

        return exclude

admin.site.register(BaseFieldModel, BaseFieldModelAdmin)
