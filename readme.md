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

    python manage.py import_original_locations

## Contact

General:
info@syrianarchive.org

Tech:
niko@syrianarchive.org




