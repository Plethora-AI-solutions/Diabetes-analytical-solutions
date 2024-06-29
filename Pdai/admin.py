from django.contrib import admin
from .models import predict, RF_model, interaction
from django.contrib.auth.models import Group

# Register your models here.



admin.site.register(predict)

admin.site.register(RF_model)

admin.site.register(interaction)




