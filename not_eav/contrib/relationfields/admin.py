from django.contrib import admin

from not_eav.admin import BaseFieldModelAdmin

from models import *

admin.site.register(ForeignKeyModel, BaseFieldModelAdmin)
