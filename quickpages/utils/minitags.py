# Copyright (c)2000-2016 Joseph J Wolff

trace = 0

def islist (x):
  if not isinstance (x, str) and (isinstance (x, list) or isinstance (x, tuple)): return True

def listdepth (o, depth=0):
  if islist (o) and len (o):
    depth += 1
    return listdepth (o [0], depth)
  else:
    return depth
  

#def iseven (n):
#  return n div 2

attrmap = dict (cls='class', fr='for', d='id')

def getattrmap (k):
  return attrmap.get (k, k)

def dict2attrs (kw):
  return ' '.join (('='.join ((getattrmap (k),'"' + str(v) + '"')) for k,v in kw.items()))


def tag (t, c, *args, **kw):  # t = tag, c = content
  if kw: attrs = ' ' + dict2attrs (kw)
  else:  attrs = ''

  if not islist (c): c = (c,)
  if args: c += args

  if trace: print t, c, args, kw

  return ''.join (['<%s%s>%s</%s>\n' % (t, attrs, i, t)  for i in c])


# ltag - this passes thru the list for filter-graph-type stream behavior - join at the end - 
# perhaps this should be the default, and str() should do the reduction?

def ltag (t, c, *args, **kw):  # t = tag, c = content
  if kw: attrs = ' ' + dict2attrs (kw)
  else:  attrs = ''

  if not islist (c): c = (c,)
  if args: c += args

  if trace: print t, c, args, kw

  return ['<%s%s>%s</%s>\n' % (t, attrs, i, t)  for i in c]


def new_shorter_tag (t, *args, **kw):  # t = tag, c = content
  #if len (args) ==1 : args = args [0] nope, still wont work.
  # still need to normalize / analyze list dimensions, here...

  if trace: print t, args, kw

  if kw: return ''.join (['<%s%s>%s</%s>\n' % (t, dict2attrs (kw), i, t)  for i in args])
  else:  return ''.join (['<%s>%s</%s>\n' % (t, i, t)  for i in args])

stag = new_shorter_tag


def leading_tag (t, *args, **kw):  # for tags like <p>, that by common usage, have no trailing tag
  pass  # NYI


def trailing_tag (t, *args, **kw):  # for tags like <br>, that, by common usage, have no leading tag
  if trace: print t, args, kw

  if listdepth (args) >1 and len (args) == 1: args = args [0]

  if kw: return ''.join (['%s<%s%s>\n' % (i, t, dict2attrs (kw))  for i in args])
  else:  return ''.join (['%s<%s>\n' % (i, t)  for i in args])  # could make xhtml-firenldy...


def tag1 (t, **kw):
  if trace: print t, kw

  return '<%s %s />\n' % (t, dict2attrs (kw))


def a     (c, *args, **kw):	return tag ('a', c, *args, **kw)
def p     (c, *args, **kw):	return tag ('p', c, *args, **kw)
def b     (c, *args, **kw):	return tag ('b', c, *args, **kw)
def tr    (c, *args, **kw):	return tag ('tr', c, *args, **kw)
def td    (c, *args, **kw):	return tag ('td', c, *args, **kw)
def th    (c, *args, **kw):	return tag ('th', c, *args, **kw)
def h1    (c, *args, **kw):	return tag ('h1', c, *args, **kw)
def h2    (c, *args, **kw):	return tag ('h2', c, *args, **kw)
def h3    (c, *args, **kw):	return tag ('h3', c, *args, **kw)
def h4    (c, *args, **kw):	return tag ('h4', c, *args, **kw)
def h5    (c, *args, **kw):	return tag ('h5', c, *args, **kw)
def h6    (c, *args, **kw):	return tag ('h6', c, *args, **kw)
def ul    (c, *args, **kw):	return tag ('ul', c, *args, **kw)
def li    (c, *args, **kw):	return tag ('li', c, *args, **kw)
def big   (c, *args, **kw):	return tag ('big', c, *args, **kw)
def div   (c, *args, **kw):	return tag ('div', c, *args, **kw)
def img             (**kw):     return tag ('img', '', **kw)
def pre   (c, *args, **kw):	return tag ('pre', c, *args, **kw)
def body  (c, *args, **kw):	return tag ('body', c, *args, **kw)
def code  (c, *args, **kw):	return tag ('code', c, *args, **kw)
def html  (c, *args, **kw):	return tag ('html', c, *args, **kw)
def form  (c, *args, **kw):	return tag ('form', c, *args, **kw)
def meta            (**kw):     return tag ('meta', '', **kw)
def span  (c, *args, **kw):	return tag ('span', c, *args, **kw)
def small (c, *args, **kw):	return tag ('small', c, *args, **kw)
def label (c, *args, **kw):	return tag ('label', c, *args, **kw)
def table (c, *args, **kw):	return tag ('table', c, *args, **kw)
def button (c, *args, **kw):	return tag ('button', c, *args, **kw)
def legend (c, *args, **kw):	return tag ('legend', c, *args, **kw)
def iframe    (*args, **kw):    return tag ('iframe', '', *args, **kw)
def strong (c, *args, **kw):	return tag ('strong', c, *args, **kw)
def select (c, *args, **kw):	return tag ('select', c, *args, **kw)
def script (c, *args, **kw):	return tag ('script', c, *args, **kw)
def fieldset (c, *args, **kw):	return tag ('fieldset', c, *args, **kw)
def textarea (c, *args, **kw):	return tag ('textarea', c, *args, **kw)

#def input (**kw):	return tag1 ('input', **kw)

def br (*args, **kw): return trailing_tag ('br', *args, **kw)


### treo - tr with even/odd row classes

#def treo (c, even=None, odd=None, *args, **kw): this doesnt work - python bugs
#def treo (c, *args, even=None, odd=None, **kw): and this doesnt syntax - grrr.
def treo (c, *args, **kw): # so do it manually w/pop
  if not islist (c): c = (c,)
  if args: c += args

  eo = 0
  s = ''

  if trace: print 'treo', c, args, kw

  even = kw.pop ('even', 'evenrow')
  odd  = kw.pop ('odd', 'oddrow')

  for row in c:
    eo = 1 - eo
    cls = None

    if eo:
      if even: cls=even
    else:
      if odd: cls=odd

    if cls: s += tr (row, cls=cls, **kw)
    else:   s += tr (row, **kw)

  return s


### option: correctly implement selected semantics, if it's false, omit it

def option (c, *args, **kw):
  assert not islist (c) and not args  # singletons only, for now

  selected = kw.pop ('selected', None)

  # later check for callable passed-in func and implement lists...

  if selected: return tag ('option', c, selected=1, **kw)
  else:        return tag ('option', c, **kw)


### optionlist: implement list of options, selected matching one in the list

from pprint import pformat, pprint

def optionlist (*args, **kw):
  selected = kw.pop ('selected', None)

  if len (args) == 1: args = args [0]
  
  if trace: print islist (args), pformat (args)

  # JJW 9/2/7 try to adapt to optional tuple passed in - normalize to o,v:
  lst = []

  for i in args:
    if islist (i): lst += [i]
    else: lst += [(i,i)]

  return ''.join ([option (o, value=v, selected=v==selected) for o,v in lst])

  #if islist (args [0]):  # assume 1st one same as the rest
  #  #return ''.join ([option (o, value=v, selected=v==selected) for arg in args for v,o in arg])
  #  return ''.join ([option (o, value=v, selected=v==selected) for o,v in args])
  #else:
  #  return ''.join ([option (v, value=v, selected=v==selected) for v in args])


### dropdown - select and optionlist - could add label, other stuff

def dropdown (*args, **kw):  # assumes you want a name in your dropdown :-)
  # name = kw.pop ('name', None)
  return select (optionlist (*args, **kw), name=kw.pop ('name', 'mydropdown'))
  

### input: correctly implement checked semantics, if it's false, omit it

def input (*args, **kw):
  assert len (args) <= 1 # a list doesn't make sense - unless you want them all checked (!)

  checked = kw.pop ('checked', None)

  # later check for callable passed-in func and implement lists...

  if checked: return tag1 ('input', checked=1, **kw)
  else:       return tag1 ('input', **kw)


# why args?  Should we include a label here?
def hidden (*args, **kw):    return input (args, type='hidden', **kw)
def checkbox (*args, **kw):  return input (args, type='checkbox', value=kw.pop ('value', None) or ' ', **kw)  # ' ' is True, but doesn't show in a commandline..
def text (*args, **kw):      return input (args, type='text', **kw)
#def button (*args, **kw):    return input (args, type='button', **kw)
def submit (*args, **kw):    return input (args, type='submit', **kw)


''' perhaps later build on passed-in options list
def select_proto (c, *args, **kw):

  selected = kw.pop ('selected', None)

  for i in c:
    pass

	return tag ('select', c, *args, **kw)
'''  
#selected=, opt id=, name=

  

if __name__ == "__main__":
  print br (1,2,3)
  print br ([4,5,6,7])

  print dropdown ([[1,2],[3,4],[5,6]])

  # someday be smart eough to know that ul with a list is the il's.. like table, tr, etc
  print ul (li ([1,2,3,4,5]))

  # ditto for select
  #print select (option ('hi there', selected=1==0, value=(1,2)))

  from sys import exit
  exit()

  psum = ['my product: default config']
  print islist (psum)
  print table (tr ([td (l.split (':')) for l in psum]), cls='summarytable')

  #print a ('one thing', href='asfgasfvgb', title='sfsfgsdfg')
	#print 3 * tr (td (['oh','so','wamy']), cls='evenrow')

	# Todo:
	#  d treo - tr even/odd
	#  ~ classes w/own attrmap

	#print th ('one','two','three')

	#rs = 3*(td(3*('data',)),)
	#print treo (rs)

  #rs = 3 * [td (3 * ['data'])]
  #print treo (rs, even='evenrow')
  #print treo (rs, th ('even','more','data'), even='evenrow')

	#lst = [1,2,3]
	#nu=(lst,)
	#print lst, nu
	#print textarea ('hi', 'there')

'''
def link (c, *args, **kw):
  if not islist (c): c = (c,)
  if args: c += args

  href = kw.pop ('href', None)  # a list of links to the same thing?!, so be it

  for i in c:
    if 
'''
