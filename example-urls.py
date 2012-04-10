# -*- coding: utf-8 -*-
#import settings

from django.conf.urls.defaults import patterns
from django.contrib import admin  # for autodiscover


### If you want to use a QuickPage for your home page, it goes at the top, like this:

urlpatterns = patterns ('quickpages.views',
    (r'^$', 'quickpage', dict (slug=None)),  # slug=None means use the page named 'index'
)

# Another way to do the same thing:

urlpatterns = patterns ('quickpages.views',
    (r'^$', 'quickpage', dict (slug='index')),
)


### [Most other urls for your project go here]


### Dynamic DB-based QuickPages:  in general, this section should be last, since it will match any pattern..

urlpatterns += patterns ('quickpages.views',
    (r'^(?P<slug>.*)/$', 'quickpage'),
)


# Here's how to pass in a custom template:

urlpatterns += patterns ('quickpages.views',
    (r'^(?P<slug>.*)/$', 'quickpage', dict (template='products/product_detail.html'))
)


# And here's an example of a custom template with additional context passed through to the custom template:

urlpatterns += patterns ('quickpages.views',
    (r'^(?P<slug>.*)/$', 'quickpage', dict (template='products/product_detail.html', prods=Product.objects.all()))
)



admin.autodiscover() # this can't be called at the top, it has to be closer to the bottom - JJW
