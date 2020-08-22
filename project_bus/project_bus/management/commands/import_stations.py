import csv
from django.core.management.base import BaseCommand

from project_bus.models import Station,Route


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(r"D:\new\creating-project\project_bus\moscow_bus_stations.csv", 'r', encoding='cp1251') as csvfile:

            station_reader = csv.reader(csvfile, delimiter=';')
            next(station_reader)

            for line in station_reader:
                station = Station.objects.create(name=line[1], latitude=line[3], longitude=line[2])
                # Station.objects.all().delete()
                # Route.objects.all().delete()
                routes_list = line[7].split(';')
                # Route.objects.bulk_create([Route(name=obj) for obj in routes_list], ignore_conflicts=True)
                # routes = Route.objects.all().order_by('-pk')[:len(routes_list)]
                # station.routes.add(*routes)
                # break
                for route in routes_list:
                    routes = Route.objects.get_or_create(name=route)
                    print(routes)
                    station.routes.add(routes[0])
                    # station.save()
