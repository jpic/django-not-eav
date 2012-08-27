from django.test import TestCase

from not_eav.forms import AttributeFormBase


class AttributeFormBaseTest(TestCase):
    def name_validation_provider(self):
        return (
            ('aoeu', True),
            ('aoeu1', True),
            ('1aoeu', False),
            ('Aaoeu', False),
            ('aoeu aeu', False),
            ('aoeu_aoe', True),
        )

    def test_001_name_validation(self):
        for test in self.name_validation_provider():
            form = AttributeFormBase(dict(name=test[0],
                content_type=1, kind='django.db.models.fields.TextField'))
            self.assertEquals(form.is_valid(), test[1])
