# Syrian Archive

The Syrian Archive is a Syrian initiative that strives to promote sustainable peace and respect for human rights within Syrian society through facilitating justice and accountability.
This includes evidence gathering and documentation of incidents; the acknowledgment that war crimes and human rights violations have been committed by all sides; the identification of perpetrators to end the cycle of impunity and the development of a process of justice and reconciliation.

more at https://syrianarchive.org/p/page/about

This is the repository holding the django application to manage the database of incidents

## Dependencies

    #basics
    django 1.8
    python 2.7
    python-virtualenv

    #mapping
    geos
    gdal

    #database
    some kind of sql
      #mysql
      python-mysql

## Features

!["Schema"](https://raw.githubusercontent.com/nikonikoniko/syrianarchive/dev/schema.png)

    completely translated database and interface into
      english
      arabic
    using
      django-modeltranslation

    mapping of incidents
      django-geojson
      django-leaflet

    filtering and searching of incidents

## Deploy

    # set up the virtual environment
    mkdir syarchenv
    cd syarchenv

    virtualenv -p /usr/bin/python2.7 .

    # enter the virtualenv
    source bin/activate

    # clone the syrianarchive django bit
    git clone DJANGO INSTALL

    cd syrianarchive

    #install python dependencies
    pip install -r requirements.txt

    #set up the databases

    create databases
      make sure the default character set is utf8!!!
      see: https://dev.mysql.com/doc/refman/5.0/en/charset-applications.html

    change sample_settings.py to settings.py
    put in DB credentials

    #create the tables in the database
    python manage.py migrate

    #add admin user
    python manage.py syncdb

    #install the location data (it is xml formatted to allow unicode arabic editing)
    python manage.py loaddata database/data/locations.xml

    #install the database metadata - International Instruments, ViolationTypes, Devices, ETC
    python manage.py loaddata database/data/database_meta_data.json

    #install the pages database... hopefully the json is kept updated
    python manage.py loaddata database/database/pages.json


## Contact

General:
info@syrianarchive.org

Tech:
niko@syrianarchive.org

## Contribute

edit translation files:
    (on dev branch please!) https://github.com/nikonikoniko/syrianarchive/blob/dev/locale/ar/LC_MESSAGES/django.po

help with design or coding:
    email niko@syrianarchive.org

help with the database:
    email info@syrianarchive.org

## Design

color scheme

    #main colors
    black: #2C2C30
    middle grey: #ACB4AC
    light grey: #E7E5E4
    white: #F5F5F4

    #primary colors:
    orange (main element): #FA7000
    teal (filters): teal
    blue (link): #0487A4
    light blue highlight: #32BDAB
    red(warning): #CC2200



#### Hacks... :(

things that have been hacked:
 - python lib static directories have been copied to /static/
  - issue for upgrade of library




