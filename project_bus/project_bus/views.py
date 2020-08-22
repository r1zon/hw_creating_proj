from django.shortcuts import render, redirect

from project_bus.models import Station, Route

def show_home(request):
    template = 'stations.html'
    routes = Route.objects.all()
    context = {'routes': routes}
    return render(
        request,
        'stations.html',
        context
    )

def show_stations(request):
    template = 'stations.html'
    route = request.GET.get('route')
    stations = Station.objects.filter(routes__name=route)
    y = (stations.first().latitude+stations.last().latitude)/2
    x = (stations.first().longitude+stations.last().longitude)/2
    center = {'x': x, 'y': y}
    context = {'stations': stations,
               'routes': Route.objects.all(),
               'center': center}
    return render(
        request,
        'stations.html',
        context
    )
