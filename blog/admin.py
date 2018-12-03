import csv


from django.contrib import admin
from django.http import HttpResponse

from .models import *
from blog.models import Comments
# Register your models here.
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


class PostAdmin(admin.ModelAdmin,ExportCSVMIXINS):
    list_display= ['title','author','created','status']
    search_fields = ['title','body']
    fields = ['title','author','duration','maxattitude','bestseason','experiencerequired','carrying','hotels','budget','location','attraction','body','status','publish','photo','photo1','photo2','photo3']
    list_filter = ['status', 'created']
    list_editable = ['status']
    list_display_links = []
    change_list_template = 'blog/change_list.html'
    actions = ['export_to_csv']

    # def export_to_csv(self,request,queryset):
    #     meta=self.model._meta
    #     field_names=[field.name for field in meta.fields]
    #     response=HttpResponse(content_type='text/csv')
    #     response['Content-Disposition']='attachment: filename=posts.csv'
    #     writer = csv.writer(response)
    #     writer.writerow(field_names)
    #     for obj in queryset:
    #         row=writer.writerow([getattr(obj,field) for field in field_names])
    #     return response
    # export_to_csv.short_description = "Export Selected posts to CSV"


admin.site.register(Post,PostAdmin)

class CommentsAdmin(admin.ModelAdmin,ExportCSVMIXINS):
    list_display = ['name','email','post_id']
    actions = ['export_to_csv']
admin.site.register(Comments,CommentsAdmin)




admin.site.register(Contact)
