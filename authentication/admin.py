from django.contrib import admin
from .models import User,Datasource,Datapoint,Telemdata

admin.site.register(User)
admin.site.register(Datasource)
admin.site.register(Datapoint)
admin.site.register(Telemdata)
