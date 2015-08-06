# Syrian Archive


## Dependencies

    django 1.8
    python 2.7
    python-virtualenv
    geos
    gdal
    some kind of sql


## Deploy

    mkdir syarchenv
    cd syarchenv

    virtualenv -p /usr/bin/python2.7 .

    source bin/activate

    git pull DJANGO INSTALL

    cd syrianarchive

    pip install -r requirements.txt

    python manage.py migrate

    change

    python manage.py import_original_locations

## Contact

General:
hadi@syrianarchive.org

Tech:
niko@syrianarchive.org




