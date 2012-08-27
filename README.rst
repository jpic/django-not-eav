.. image:: https://secure.travis-ci.org/yourlabs/django-not-eav.png?branch=master

This app attempts the impossible: implement a bad idea the right way.

Concept
-------

``django-not-eav`` provides a special model: ``Attribute``.

When such a model is created:

- a model field is generated and added to the corresponding model class
  dynamically,
- a column is created, using ``south`` API,
- the admin is reloaded'

``not_eav.autodiscover()`` is in charge of iterating over all ``Attribute`` to
add the model fields to the model class dynamically.

You can add or remove fields in the admin, but you may not change a field name
or type.

The advantage of this pattern over classic eav `heavy solutions
<https://bitbucket.org/neithere/eav-django/src/tip/eav/models.py>`_ is that
dynamic fields can be treated like regular fields.

The inconvenient is that it gives the website administrator the opportunity to
mess up with his database.

In the end, this app enables the website administrator to become the developer
of his own application.

This app will be the base requirement for the 3 upcomming apps, enabling the
website administrator to:

- create his forms,
- create his list views,
- create his details views,

Requirements
------------

- Python 2.7
- South
- Django 1.4+

Resources
---------

You could subscribe to the mailing list ask questions or just be informed of
package updates.

- `Mailing list graciously hosted
  <http://groups.google.com/group/yourlabs>`_ by `Google
  <http://groups.google.com>`_
- `Git graciously hosted
  <https://github.com/yourlabs/django-not-eav/>`_ by `GitHub
  <http://github.com>`_,
- `Documentation graciously hosted
  <http://django-not-eav.rtfd.org>`_ by `RTFD
  <http://rtfd.org>`_,
- `Package graciously hosted
  <http://pypi.python.org/pypi/django-not-eav/>`_ by `PyPi
  <http://pypi.python.org/pypi>`_,
- `Continuous integration graciously hosted
  <http://travis-ci.org/yourlabs/django-not-eav>`_ by `Travis-ci
  <http://travis-ci.org>`_

Demo
----

See test_project/README
