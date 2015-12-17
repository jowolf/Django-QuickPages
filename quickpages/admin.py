# encoding: utf-8

from django.contrib import admin

from apps.utils import created, updated, publish, unpublish
from quickpages.models import QuickPage, QuickSnippet


#### Globals

trace = 0


#### Admin classes

class QuickPageAdmin (admin.ModelAdmin):
    change_form_template = 'quickpages/admin_wysiwyg_change_form.html'

    fieldsets  = (
                  (None, {'fields': (('name', 'slug'), ('title', 'published'),)}),
                  ('Extras', {'classes': ('collapse',), 'fields': (('javascript','css'), 'heading')}),
                  ('Meta', {'classes': ['collapse'], 'fields': ('meta_title','description','keywords')}),
                  ('Comments', {'classes': ['collapse','noedit'], 'fields': ('comments',)}),
                  ('Content', {'classes': ['edit'], 'fields': ('content','template')}),  # , 'wide' is NFG
                  #('Content', {'classes': ['codemirroreditor'], 'fields': ('content','template')}),  # , 'wide' is NFG
                 )

    list_filter = ('published', 'created', 'updated', 'template')
    list_display = ('name', 'slug', 'title', 'template', 'published', 'comments', created, updated)
    search_fields = ('name','slug','title', 'template','meta_title','description','keywords')
    save_as = True
    prepopulated_fields = {"slug": ("name",)}

    #class Media:
    #    js = ('/media/tinymce/tiny_mce.js','/media/tinymce/mce_setup.js')


def tags (instance):
    return ','.join (instance.tags.values_list ('name', flat=True))

tags.short_description = 'Tags'
tags.description = 'Tag(s) for this object'
tags.allow_tags = True

class QuickSnippetAdmin (admin.ModelAdmin):
    change_form_template = 'quickpages/admin_wysiwyg_change_form.html'

    list_display = ('name', 'title', tags, 'js', 'css', 'body', 'comments', 'published', created, updated)
    #list_filter = ('published','created','updated')
    search_fields = ('name', 'title', 'js', 'css', 'body', 'comments')
    #list_editable = ('link', 'title', 'caption', 'published', 'sortorder',)
    list_per_page = 50
    save_as = True
    actions = [publish, unpublish]

    #class Meta:
    #    proxy = True

admin.site.register (QuickPage, QuickPageAdmin)
admin.site.register (QuickSnippet, QuickSnippetAdmin)
