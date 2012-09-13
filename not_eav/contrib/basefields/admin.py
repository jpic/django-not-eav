from django.contrib import admin

from not_eav.admin import BaseFieldModelAdmin

from models import *


admin.site.register(BooleanFieldModel, BaseFieldModelAdmin)
admin.site.register(CharFieldModel, BaseFieldModelAdmin)
admin.site.register(DateFieldModel, BaseFieldModelAdmin)
admin.site.register(DateTimeFieldModel, BaseFieldModelAdmin)
admin.site.register(DecimalFieldModel, BaseFieldModelAdmin)
admin.site.register(EmailFieldModel, BaseFieldModelAdmin)
admin.site.register(IntegerFieldModel, BaseFieldModelAdmin)
admin.site.register(IPAddressFieldModel, BaseFieldModelAdmin)
admin.site.register(NullBooleanFieldModel, BaseFieldModelAdmin)
admin.site.register(PositiveIntegerFieldModel, BaseFieldModelAdmin)
admin.site.register(TextFieldModel, BaseFieldModelAdmin)
admin.site.register(TimeFieldModel, BaseFieldModelAdmin)
admin.site.register(URLFieldModel, BaseFieldModelAdmin)
