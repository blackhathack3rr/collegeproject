import csv

from business.models import Business,Add
from django.contrib import admin
from business import models
# Register your models here.
from django.http import HttpResponse


class ExportCSVMIXINS():
    def export_to_csv(self,request,queryset):
        meta=self.model._meta
        field_names=[field.name for field in meta.fields]
        response=HttpResponse(content_type='text/csv')
        response['Content-Disposition']='attachment: filename=posts.csv'
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row=writer.writerow([getattr(obj,field) for field in field_names])
        return response

    export_to_csv.short_description = "Export Selected posts to CSV"


class Com(admin.ModelAdmin,ExportCSVMIXINS):
    list_display = ['name','location','phone','price','offers','hotelfacilities','roomfacilities','inhouseservice','photo','photo1']
    actions = ['export_to_csv']
admin.site.register(Add,Com)

class Co(admin.ModelAdmin,ExportCSVMIXINS):
    list_display = ['buser','email','phone','pas']
    actions = ['export_to_csv']
admin.site.register(Business,Co)

