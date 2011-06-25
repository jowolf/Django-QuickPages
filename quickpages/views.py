# encoding: utf-8

from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
#from django.http import HttpResponse
#from django.conf import settings

from quickpages.models import QuickPage
from quickpages.minitags import h1


### Globals

trace = 0


### helpers, should go into helpers.py:

def crumbs (req, o=None): 		# one level added to Home - extract name, title fm obj o
  crumbs = [ link ('Home', href="/", title="Libre Hosting Home Page"), ]

  if not o: return crumbs [0]

  if hasattr (o, 'view_func'):		# its a decorated func, chase it
    o = o.view_func

  if hasattr (o, 'func_name'):		# it's a view function
    nam   = o.func_name.capitalize()
    title = o.func_doc
  elif hasattr (o, 'name'):		# it's a db page object
    nam = o.name
    title = o.title
  else:
    raise Exception, 'Invalid object in hosting.views.crumbs'

  crumbs += [ link (nam, href=req.path, title=title) ]
  return ' :: '.join (crumbs)


### QuickPages view - 'generic' db view, with meta tags, titles, js/css, etc

def quickpage (request, name=None, template='quickpages/base.html', breadcrumbs=True, **kw):
    if name:
        page = get_object_or_404 (QuickPage.objects, name=name)
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


























### reload the snippets dict
old='''
def reloadsnippets (req):
  loadsnippets()
  s = 'Snippets reloaded'
  return resp (req, title=s, content=s)


def dbpage (req, name, **kw):
  page = get_object_or_404 (Page.objects, name=name)
  crumb = page

  js = page.javascript
  if js: js = jstags (js.split())

  print `snippets`

  content = page.content % snippets
  content = h2 (page.title) + content

  kw = dict (name=page.name,
	title=page.title,
	content=content,
	keywords=page.keywords,
	description=page.description,
	breadcrumbs=crumbs (req, crumb),
	javascript=js or defaultjs
	)

  return resp (req, **kw)
'''

# currently only wired to 'test'- JJW 9/3/8
def index (req):
  #'Libre hosting&trade; plan offerings'
  #good   = Product.objects.get (slug='standard')
  #better = Product.objects.get (slug='professional')
  #best   = Product.objects.get (slug='enterprise')

  #def pln (s): return render_monthly_hosting_plan (s, True)

  #content = h2 ('Featured Hosting Plans', cls='title') + \
  #	    div (pln (good) + pln (better) + pln (best), cls='plans')

  page = get_object_or_404 (Page.objects, name='index')

  js = page.javascript
  if js: js = jstags (js.split())

  content = h2 (page.title) + page.content
  return resp (req, name=page.name,
                    title=page.title,
                    content=content,
                    keywords=page.keywords,
                    description=page.description,
                    javascript=js or defaultjs,
                    breadcrumbs=crumbs (req))


old_plans='''
import csv
def plans (req):
  'Comparison grid of Libre Hosting&trade; plans'
  rowlist = [r for r in csv.reader (open ("/root/libre/hosting/LibreHostingPlanGrid.csv", "rb"))]

  rows = [th (rowlist [0])]

  for row in rowlist [1:-1]:
    rows += [td (row)]

  rows += [th (rowlist [-1])]

  # thegrid = table (tr (rows), border=1, cellpadding=5, cls='grid')
  thegrid = table (treo (rows), cls='grid')
  return resp (req, 'grid.html', 
                    grid=thegrid, 
                    javascript=defaultjs,
                    title=mydoc(plans),
                    breadcrumbs=crumbs (req, plans))
'''


def uptime (req):
  'Libre Hosting&trade; - Host system uptime'
  content = h1 ("Libre host system uptime:") + h4 (kvm.sh ('uptime'))
  return resp (req, content=content, javascript=defaultjs, title=mydoc(uptime), breadcrumbs=crumbs (req))

from django import forms
from django.forms import ModelForm, Form
from libre.opt.models import NestedOption

class InstanceForm(ModelForm):
  class Meta:
    model = Instance

class PlanForm(ModelForm):
  class Meta:
    model = Plan

class NestedOptionForm(ModelForm):
  class Meta:
    model = NestedOption

class MyNestedForm(Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


# util fn
def getleaves (lst):
  lst2 = []
  lst3 = []
  sep = ' + '

  # first break out the right-hand lists into individual line items
  for ll, rl in lst:
    l = sep.join(ll)
    if len (rl) > 1:
      for r in rl:
        lst2.append (l + sep + r)
    else:
      lst2.append (l + sep + rl [0])

  print pformat (lst2)

  # now collapse the dups:
  lst4 = lst2[:]
  while len (lst4) > 0:
    l = lst4.pop(0)
    found = 0
    for l2 in lst2:
      print 'l:', l, ':l2:', l2
      if l != l2 and l2.startswith (l):
        found = 1
        print 'found:', l
        break
    if not found: lst3.append (l)

  #print pformat (lst3)

  return lst3


def instances (req):
  'Libre Hosting Instance & Plan test page'

  instform = InstanceForm()
  #planform = PlanForm()
  nestform = NestedOptionForm()
  mynestform = MyNestedForm()

  plan = Plan.objects.get(pk=1)
  frm = PlanForm(instance=plan)

  #if req.method == 'POST':
  #  form = PlanForm(req.POST)
  #  if form.is_valid():
  #    # Do form processing here...
  #    return HttpResponseRedirect('/url/on_success/')

  #frm = PlanForm()
  c = h2('The NestedOpts Form') + table (nestform.as_table()) + \
      h2('My Nested Form') + table (mynestform.as_table()) + \
      h2('The Plan Form') + frm.as_p() + \
      h2('The Instance Form') + instform.as_p()


  # OK lets use mine, JJW 9/21/08
  from libre.hosting.ttree import parselist, lst, old_lst

  if req.method == 'POST':
    c = '<h3>'

    for k,l in sorted(req.POST.lists()):
      c += k + '<br>'
      c += '&nbsp;&nbsp;&nbsp;&nbsp;' + ', '.join (l) + '<br>'

    c += '<hr>'

    for k,l in sorted(req.POST.lists()):
      c += '&nbsp;' * len (k.split ('.')) + ', '.join (l) + '<br>'

    c += '<hr>'

    for k,l in sorted(req.POST.lists()):
      toks = k.split ('.')
      c += '&nbsp;' * len (toks) + toks [-1] + ': ' + ', '.join (l) + '<br>'

      #toks = k.split ('.')
      #for t in toks: tree [t]

    lst = req.POST.lists()
    #dct = dict (lst)
    lst = [(n.split('.'), v) for n,v in lst]
    #lst.sort (key=lambda x: len(x[0]))
    #lst = [(k [0], k[1:] + v) for k,v in lst]
    #c = pre (pformat (lst).replace ('<','{'))
    #c = '<br>'.join ([': '.join(itm[0]) + ':: ' + ', '.join(itm [1]) for itm in lst])

    lst = getleaves (lst)
    #print lst

    dct = {}
    lst = [l.split(' + ', 1) for l in lst]

    for k,v in lst:
      dct [k] = dct [k] + [v] if k in dct else [v]

    #print dct

    c = pre (pformat (dct))
    #c = pre (pformat (getleaves (lst)))

    opts = []
    for k,v in dct.items():
      opts += ['%s options: %s' % (k.replace ('_',' '), '<br>'.join (v))]

    c += para (opts)
    c += '<hr>'

  else:
    c = form (parselist (lst) + '<br>' +
              input (type='submit',
                     value='Save Configuration Wishlist'),
              method='POST',
              d='ttree') + \
        div (' ',  d='statusdiv')
              #action = '/to/shop/cart?'
    #c = ttreeform (lst, '.') # + '<hr>' + parselist (old_lst)


  return resp (req,
               content=c,
               javascript=defaultjs + jstags (['ttree.js'])
              )
  #render_to_response('contact.html', {'form': form})



def descriptions (req, pth):
  'Libre Hosting Options Tree Description page'

  post = Post.objects.filter (title=pth)

  if post:
    c = post [0].body
  else:
    c = 'No Description Found.'

  if req.is_ajax():
    return HttpResponse (div (c, d='description')) # , style='max-width:300px; background-color:wheat;')
  else:
    return resp (req,
                 title=unslugify (pth),
                 content=c,
                 javascript=defaultjs # + jstags (['ttree.js'])
                )
