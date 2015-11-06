# encoding: utf-8

from django.contrib import admin

from quickpages.models import QuickPage


#### Globals

trace = 0


#### Admin stuff

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
    list_display = ('name', 'slug', 'title', 'template', 'published', 'comments', 'created', 'updated')
    search_fields = ('name','slug','title', 'template','meta_title','description','keywords')
    save_as = True
    prepopulated_fields = {"slug": ("name",)}

    #class Media:
    #    js = ('/media/tinymce/tiny_mce.js','/media/tinymce/mce_setup.js')


admin.site.register (QuickPage, QuickPageAdmin)


#### Move obdjects.snippets into here for cleaner admin 6/10/12 JJW

# NOTE 6/22-23/12 JJW:
# Django bug, caused by incorrect app label on content type, sommehow:
# 'NoneType' object has no attribute '_meta'
# Solution is to use ProxyModel and change the name, I guess

from obdjects.models import Snippet
from obdjects.admin import SnippetAdmin

try:
    admin.site.unregister (Snippet)
    if trace: print 'successfully unregistered Snippet'
except Exception, e:
    print e
    raise

# Nope, doesn't work:
# class MySnippetAdmin (SnippetAdmin):
#    pass

# Nope, doesn't work:
# Snippet._meta.app_label = u'quickpages'

# So try proxy model:

class QuickSnippet(Snippet):
    save_as = True

    class Meta:
        proxy = True

try:
    #admin.site.register (Snippet, MySnippetAdmin)
    #admin.site.register (Snippet, SnippetAdmin)
    admin.site.register (QuickSnippet, SnippetAdmin)
    if trace: print 'successfully re-registered QuickSnippet under QuickPages'
except Exception, e:
    print e
    raise
