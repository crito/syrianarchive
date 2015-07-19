from django.core.management.base import BaseCommand, CommandError
from database.models import LocationPlace
from syrianarchive.site_settings import BASE_PATH
import json
from django.shortcuts import get_object_or_404, render

class Command(BaseCommand):
    help = "Imports locations from json file - Forein keys wont work any more -- deletes old.  for site deploy"
    def add_arguments(self, parser):
        pass
    def handle(self, *args, **options):
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

                print "========================="
                print "newlocation:"
                print "name : ", new_location.name_en
                print "name_ar : ", new_location.name_ar
                print "id : ", new_location.dataset_id
                print "lat : ", new_location.latitude
                print "lon : ", new_location.longitude
                print "region : ", new_location.region.name
                print "======================="

