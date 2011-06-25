# encoding: utf-8

from django.contrib import admin

from quickpages.models import QuickPage



class QuickPageAdmin (admin.ModelAdmin):
    fieldsets  = (
                  (None, {'fields': (('name', 'title', 'published'),)}),
                  ('Extras', {'classes': ['collapse'], 'fields': (('javascript','css'), 'heading')}),
                  ('Meta', {'classes': ['collapse'], 'fields': ('description','keywords')}),
                  ('Comments', {'classes': ['collapse','noedit'], 'fields': ('comments',)}),
                  (None, {'classes': ['edit'], 'fields': ('content',)}),  # , 'wide' is NFG
                 )

    list_filter = ('published', 'created', 'updated')
    list_display = ('name', 'title', 'published', 'comments', 'created', 'updated') 
    save_as = True

    class Media:
        js = ('/media/tinymce/tiny_mce.js','/media/tinymce/mce_setup.js')


admin.site.register (QuickPage, QuickPageAdmin)

