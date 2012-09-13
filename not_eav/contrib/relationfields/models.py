from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType

from not_eav.models import BaseFieldModel


class ForeignKeyModel(BaseFieldModel):
    module_class = 'django.db.models.fields.related.ForeignKey'
    related_to = models.ForeignKey(ContentType)
    related_to.not_changeable = True

    def field_kwargs(self):
        kwargs = super(ForeignKeyModel, self).field_kwargs()
        kwargs['to'] = self.related_to.model_class()

        # enforce null=True since we're adding this on an existing table
        # but it shouldn't matter since we leave blank=False
        kwargs['null'] = True

        return kwargs

    class Meta:
        verbose_name = _(u'Foreign key')
