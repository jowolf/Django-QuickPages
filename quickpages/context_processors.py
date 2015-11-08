"""
Django QuickPages request processors that return dictionaries to be merged into a
template context. Each function takes the request object as its only parameter
and returns a dictionary to add to the context.

These are referenced from the setting TEMPLATE_CONTEXT_PROCESSORS and used by
RequestContext.
"""

from django.conf import settings as django_settings
from django.db.models import get_models, Manager
from django.utils.safestring import mark_safe

from quickpages.models import QuickSnippet
from taggit.models import TaggedItem


#### module globals

trace = 0


#### Utility classes, functions, & globals to hold returned data

class StringObject (unicode):
    pass

def _get_snippets():
    result = {}
    js = ''
    css = ''
    script_tags = ''
    link_tags = ''

    for obj in QuickSnippet.objects.published():
        s = StringObject (obj.body)
        s = mark_safe (s)
        s.object = obj
        result [obj.name] = s

        if obj.js:
          if obj.js.strip().lower().startswith ('<script'):  # pass thru verbatim
            scripts += obj.js + '\n'
          else:
            js += obj.js + '\n'

        if obj.css:
          if obj.css.strip().lower().startswith ('<link'):  # pass thru verbatim
            links += obj.css + '\n'
          else:
            css += obj.css + '\n'

    if css:
      css = '<style>\n%s\n</style>\n' % css

    if js:
      js = '<script type="text/javascript">\n%s\n</script>\n' % js

    result ['quick_styles'] = link_tags + css
    result ['quick_scripts'] = script_tags + js
    return result

snippets = _get_snippets()


def _get_tags():  # returns dict of lists of taggged items indexed by tag name
    result = {}

    #for ti in TaggedItem.objects.all():
    #  results [ti.tag.name] = (results [ti.tag.name] + [ti.object]) if results [ti.tag.name] else [ti]

    for t in QuickSnippet.tags.all():
      snips = [ti.content_object for ti in t.taggit_taggeditem_items.all()]
      result [t.name] = (result [t.name] + snips) if t.name in result else snips

    return result

tags = _get_tags()


#### Context Processors

def quick_snippets (request):
    if request.path.startswith (('/files', '/admin')):  # collides with admin, django_bfm
        return {}

    return snippets


def quick_snippet_tags (request):
    if request.path.startswith (('/files', '/admin')):  # collides with admin, django_bfm
        return {}

    return tags



#### main, for testing - NFG Django 1.7, all sorts of catch-22 sh*t with django.setup() - see myproject.py, but has to be in the same dir. grr.

if __name__ == '__main__':

    print quick_snippets (None)
    print quick_styles (None)
    print quick_scripts (None)
