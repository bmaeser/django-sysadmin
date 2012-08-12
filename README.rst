===============
django-sysadmin
===============

************
Installation
************

with pip as easy as: ::

    $ pip install django-sysadmin

or checkout the latest version from github: ::

    $ git clone https://github.com/bmaeser/django-sysadmin.git
    $ cd django-sysadmin
    $ python setup.py

*******
Modules
*******

Postfix
=======

Dependencies
------------------

for virtual_mailbox_domains, virtual_mailbox_maps and virtual_alias_maps you need your postfix to be configured to use your prefered database. on ubuntu the necessary packages are:

for mysql support ::

    $ apt-get install postfix-mysql

or for postgresql support :: 

    $ apt-get install postfix-pgsql

sasl2 authentication against a database needs ::

    $ apt-get install libsasl2-2 libsasl2-modules libsasl2-modules-sql

in sample-config you find some templates for your postfix configuration against postgresql

Usage
------------------

add django_sysadmin.postfix to installed apps in your django settings.ps ::

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.staticfiles',
        'django.contrib.admin',
        'django_sysadmin.postfix',   <---
    )

fire up your admin and you are done.