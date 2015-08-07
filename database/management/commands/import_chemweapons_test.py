# coding: utf-8
from django.core.management.base import BaseCommand, CommandError
from database.models import LocationPlace, DatabaseEntry, ViolationType
from syrianarchive.site_settings import BASE_PATH
import json
import csv
from django.shortcuts import get_object_or_404, render
from djgeojson.fields import PointField, PolygonField
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import Point, LineString, MultiLineString


class Command(BaseCommand):
    help = "Imports locations from json file - Forein keys wont work any more -- deletes old.  for site deploy"
    def add_arguments(self, parser):
        pass
    def handle(self, *args, **options):
        print "Imports the testing spreadsheet of chemical weapons attacks"
        var = raw_input("warning: this will remove all data from the Incidents database, resetting them to their original state.  are you sure? (yes): ")
        print "you entered", var
        if var != "yes":
            return

        DatabaseEntry.objects.all().delete()
        notfound = []

        def find_location(location_string):
          locations = LocationPlace.objects.filter(name_en__icontains=location_string)
          location = None
          if locations:
            location = locations[0]
            print "found! %s", location
          else:
            print location_string, "not found"
            notfound.append(location_string)
          return location

        def latlon_conversion(old):
          direction = {'N':-1, 'S':1, 'E': -1, 'W':1}
          new = old.replace(u'°',' ').replace('\'',' ').replace('"',' ')
          new = new.split()
          new_dir = new.pop()
          new.extend([0,0,0])
          if "." in str(new_dir):
              return old
          else:
              return (int(new[0])+int(new[1])/60.0+int(new[2])/3600.0) * direction[new_dir]

        print BASE_PATH
        with open( BASE_PATH + '/database/data/chemweap.csv', 'r') as f:
          reader = csv.DictReader(f, (
                "id",
                "location",
                "location_ar",
                "lon",
                "lat",
                "accuracy",
                "time",
                "summary",
                "violationtype",
                "weapons",
                "sources",
                "sources_ar",
                "online_url",
                "videolink"))
          print reader
          #print [ row["id"] for row in reader ]
          print reader
          next(reader)
          for row in reader:
            print "hi"
            entry = DatabaseEntry.objects.create(
              name = row["id"],
              reference_code = row["id"],
              staff_id = "import script",
              location = find_location(row["location"]),
              location_latitude = row["lat"],
              location_longitude = row ["lon"],
              #time = parse_date(row["time"]),
              description = row["summary"],
              #type_of_violation = find_violationtype(row["violationtype"]),
              weapons_used = row["weapons"],
              acquired_from = row["sources"],
              #source_connection = row["sources"],
              #recording_date
              video_url = row["videolink"],
              online_link = row["online_url"],
              online_title = "",
              graphic_content = True
              )

            if entry.location_longitude and entry.location_latitude:
              print "adding geom"
              geofield = {'type': 'Point', 'coordinates': [float(latlon_conversion(entry.location_longitude)), float(latlon_conversion(entry.location_latitude))]}
              entry.geom = geofield
              entry.save()
              print entry.geom

            print entry.name
          print [ loc for loc in notfound]

