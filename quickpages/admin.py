# encoding: utf-8

from django.contrib import admin

from quickpages.models import QuickPage



class QuickPageAdmin (admin.ModelAdmin):
  fieldsets  = (#(None, {'fields': ('site', 'name', 'title', 'typ')}),
                (None, {'fields': (('name', 'title', 'published'),)}),
                ('Extras', {'classes': ['collapse'], 'fields': (('javascript','css'), 'heading')}),
                #('Extras', {'classes': ['collapse'], 'fields': (('javascript','css'), ('heading', 'headingtag'))}),
                ('Meta', {'classes': ['collapse'], 'fields': ('description','keywords')}),
                ('Comments', {'classes': ['collapse','noedit'], 'fields': ('comments',)}),
                (None, {'classes': ['edit'], 'fields': ('content',)}),  # , 'wide' is NFG
               )

  list_display = ('name', 'title', 'published', 'comments') 
  save_as = True

  class Media:
    js = ['/tiny_mce/tiny_mce.js', '/js/textareas.js'] # JJW 7/4/07, 3/20/08


admin.site.register (QuickPage, QuickPageAdmin)

