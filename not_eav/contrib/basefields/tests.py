import decimal
import datetime
import unittest

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.utils.timezone import utc

from unittest_data_provider import data_provider

from models import *


NOW = datetime.datetime.utcnow().replace(tzinfo=utc)
USER_CTYPE = ContentType.objects.get_for_model(User)


class FieldModelTest(unittest.TestCase):
    def get_user(self):
        u, c = User.objects.get_or_create(username='test')
        return u

    def provider():
        return (
            (BooleanFieldModel, 'boolean', True),
            (CharFieldModel, 'char', 'foo', {'max_length': 12}),
            (DateFieldModel, 'date', datetime.date.today()),
            (DateTimeFieldModel, 'datetime', NOW),
            (DecimalFieldModel, 'decim', decimal.Decimal('123.22'), {
                'max_digits': 7, 'decimal_places': 3}),
            (EmailFieldModel, 'email', 'foo@example.com'),
            (IntegerFieldModel, 'int', -1231),
            (IPAddressFieldModel, 'ip', '123.213.123.123'),
            (NullBooleanFieldModel, 'nullbool', None),
            (PositiveIntegerFieldModel, 'posint', 123),
            (TextFieldModel, 'text', 'aoeuidht'),
            (TimeFieldModel, 'time', datetime.time(2, 3)),
            (URLFieldModel, 'url', 'http://example.com'),
        )

    @data_provider(provider)
    def test_001(self, cls, name, value, kwargs=None):
        if kwargs is None:
            kwargs = {}

        field = cls(name=name, content_type=USER_CTYPE, **kwargs)
        field.save()

        user = self.get_user()
        setattr(user, name, value)
        user.save()

        user = self.get_user()
        self.assertEqual(getattr(user, name), value)
        self.assertEqual(User.objects.filter(**{name: value}).count(), 1)

        field.delete()
        user = self.get_user()
        self.assertEqual(hasattr(user, name), False)
