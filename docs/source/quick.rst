Quick start
===========

The purpose of this documentation is to get you started as fast as possible,
because your time matters and you probably have other things to worry about.

Quick install
-------------

Install the package::

    pip install django-not-eav
    # or the development version
    pip install -e git+git://github.com/yourlabs/django-not-eav.git#egg=django-not-eav

Add to INSTALLED_APPS::

    'not_eav'

Add before admin.autodiscover()::

    import not_eav
    not_eav.autodiscover()

This will iterate over all ``Attribute`` objects, adding the dynamic fields to
the corresponding models.
