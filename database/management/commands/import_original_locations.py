from django.core.management.base import BaseCommand, CommandError
from database.models import LocationPlace
from syrianarchive.site_settings import BASE_PATH
import json
from django.shortcuts import get_object_or_404, render
from djgeojson.fields import PointField, PolygonField
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import Point, LineString, MultiLineString


class Command(BaseCommand):
    help = "Imports locations from json file - Forein keys wont work any more -- deletes old.  for site deploy"
    def add_arguments(self, parser):
        pass
    def handle(self, *args, **options):
        print "Imports locations from json file - Forein keys wont work any more -- deletes old.  for site deploy"
        var = raw_input("warning: this will remove all data from the location database, resetting them to their original state.  are you sure? (yes): ")
        print "you entered", var
        if var != "yes":
            return

        current_locations = LocationPlace.objects.all()
        print BASE_PATH
        with open( BASE_PATH + '/database/data/locations.json', 'rU') as f:
            locations = json.load(f)
            LocationPlace.objects.all().delete()
            for location in locations:
                print location["name"]

                new_location = LocationPlace.objects.create(
                    name_en = location["name"],
                    name_ar = location["arabic_name"],
                    dataset_id = location["id"],
                    latitude = location["latitude"],
                    longitude = location["longitude"],
                    )

                new_location.save()

                try:
                    region = get_object_or_404(LocationPlace, name = location["region"])
                except:
                    region = new_location

                new_location.region = region
                new_location.save()

                geofield = {'type': 'Point', 'coordinates': [float(new_location.longitude), float(new_location.latitude)]}
                print "aaaaaaaaa", geofield

                new_location.geom = geofield

                new_location.save()

                print "========================="
                print "newlocation:"
                print "name : ", new_location.name_en
                print "name_ar : ", new_location.name_ar
                print "id : ", new_location.dataset_id
                print "lat : ", new_location.latitude
                print "lon : ", new_location.longitude
                print "geom : ", new_location.geom
                print "region : ", new_location.region.name
                print "======================="

