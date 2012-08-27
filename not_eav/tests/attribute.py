from django.test import TestCase

import not_eav
from not_eav.models import Attribute

from book.models import Book

not_eav.autodiscover()


class AttributeTest(TestCase):
    def test_001_new_charfield(self):
        Attribute.factory(Book, name='new_charfield',
            kind='django.db.models.fields.CharField').save()

        book = Book(name=u'Breaking Django', new_charfield='Easy !')
        book.save()

        book = Book.objects.get(name=u'Breaking Django')
        self.assertEquals(book.new_charfield, 'Easy !')
