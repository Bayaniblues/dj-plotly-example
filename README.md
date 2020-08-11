# Django plotly

First install django plotly dash, this installs everything from django to plotly dash

    pip install django_plotly_dash
    
Then lets start project with this command for django

    django-admin startproject dj-plotly
    
configure settings.py to accept plotly dash

    INSTALLED_APPS = [
        ...
        'django_plotly_dash.apps.DjangoPlotlyDashConfig',
        ...
        ]
        
    X_FRAME_OPTIONS = 'SAMEORIGIN'

The application routes need to be registered within the routing structure at settings.py

    urlpatterns = [
        ...
        path('django_plotly_dash/', include('django_plotly_dash.urls')),
    ]
    
Then apply the setting with the migrate command. This also builds our 
database.

    python manage.py migrate
    
## Building an app
    
Django is a framework that can operate multiple apps in one. Start a new app with startapp command 

    python manage.py startapp plotlyapps
    
Add our new app to settings.py

    INSTALLED_APPS = [
        'plotlyapps',
    
Build our template that will be our dashboard, create files templates/index.html

    {% load static %}
    <!DOCTYPE html>
    <html>
    <head>
        <title>{% block title %} {% endblock %}</title>
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    
        <!-- Compiled and minified CSS -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
    
        <!-- Compiled and minified JavaScript -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
    
        <link href="{% static 'css/base.css'%}" rel="stylesheet">
        <script src="{% static 'js/main.js'%}"></script>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    </head>
    <body>
        <h1>Hello plotly</h1>
    </body>
    </html>    
    
    
Django is based on the model-view-template paradigm

    from django.shortcuts import render
    
    def index(request):
        return render(request,
                      'index.html')


