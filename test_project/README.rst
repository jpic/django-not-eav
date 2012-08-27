test_project: basic features and examples
=========================================

Virtualenv is a great solution to isolate python environments. If necessary,
you can install it from your package manager or the python package manager,
ie.::

    sudo easy_install virtualenv

Install last release
--------------------

Install packages from PyPi and the test project from Github::

    rm -rf django-not-eav not_eav_env/

    virtualenv not_eav_env
    source not_eav_env/bin/activate
    git clone https://github.com/yourlabs/django-not-eav.git
    cd django-not-eav/test_project
    pip install -r requirements.txt
    ./manage.py runserver

Or install the development version
----------------------------------

Install directly from github::

    NOT_EAV_VERSION="master"

    rm -rf not_eav_env/

    virtualenv not_eav_env
    source not_eav_env/bin/activate
    pip install -e git+git://github.com/yourlabs/django-not-eav.git@$NOT_EAV_VERSION#egg=not_eav
    cd not_eav_env/src/not-eav/test_project
    pip install -r requirements.txt
    ./manage.py runserver

Usage
-----

- Run the server,
- Connect to `/admin/`, ie. http://localhost:8000/admin/,
- Login with user "test" and password "test",
- Create an attribute on the book content type,
- Open add page for Book model,
- Use your new field

Database
--------

A working SQLite database is shipped, but you can make your own ie.::

    cd test_project
    rm -rf db.sqlite
    ./manage.py syncdb --noinput
