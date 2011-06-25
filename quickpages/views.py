# encoding: utf-8

from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
#from django.http import HttpResponse
#from django.conf import settings

from quickpages.models import QuickPage
from quickpages.utils import jstags, csstags
from quickpages.utils.minitags import h1


### Globals

trace = 0


### View functions


# QuickPages view - 'generic' db view, with meta tags, titles, js/css, etc

def quickpage (request, name=None, template='quickpages/base.html', breadcrumbs=True, **kw):
    if name:
        page = get_object_or_404 (QuickPage.objects.filter (published=True), name=name)
        #crumb = page
    else:  # it's the 'index' page - /
        page = get_object_or_404 (Page.objects, name='index')
        #crumb = None

    if trace: print 'QuickPage:', page

    js = page.javascript
    if js: js = jstags ([s.strip() for s in js.split(',')])

    css = page.css
    if css: css = csstags ([s.strip() for s in css.split(',')])

    if page.heading:
        content = h1 (page.title) + page.content
    else:
        content = page.content

    kw.update (dict (name=page.name,
        title=page.title,
        content=content,
        keywords=page.keywords,
        description=page.description,
        breadcrumbs=breadcrumbs,
        javascript=js,
        css=css,
        )
    )

    return render_to_response (template, kw, context_instance=RequestContext(request))
