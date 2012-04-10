Django-QuickPages
=================

Simliar to django-flatpages, but better & more flexible:

- Allows for meta tags: content, keywords for SEO
- Separate fields for slug, name & title
- URLs are placed directly in your URLs - no magic
- Context can be passed through from url declarations
- Does not require or use middleware, therefore plays nice with Django Debug Toolbar (DjDT)
- Allows for added / included JavaScript and CSS assets
- More flexible URL configuration and usage
- Optional page header included in content
- Integrates with Django-TinyMCE if present
- Integrates with FileBrowser if present, Allows for image assets


Requirements:
-------------

- Tested with Django 1.3 & 1.4, likely compatible with earlier & later versions as well.
- Effort was made to use only more generic Django features to ensure wider compatibility.  Let me know if you have problems.


Installation:
-------------

- Check out the Django-QuickPages repo into your local source location - we use /usr/local/src.
- Symlink the inner "quickpages" folder into your python path (eg, /usr/local/lib/python2.7/dist-packages on Ubuntu 11.04)
- Add 'quickpages' to your INSTALLED_APPS
- Add the appropriate urls to your root urls.py as described under 'Usage', following the example_urls.py examples.


Usage:
------

- Integrate into your root urls.py following the examples in example_urls.py
- Can be used for your home page per the examples
- If a custom template is desired, copy the example from quickpages/base.html to <yourproject>/templates/quickpages/base.html,
- Then customize accordingly
- You can also use a different template name, and siumply pass it in in the url declaration, see the examples
- Additional context, even a db model query, can be passed though to the custom template - again see the examples-url.py.
- PublishedManager to preselect only piblished or unnpublished objects - simply use: QuickPages.objects.published, or QuickPages.objects.unpublished


Added April, 2012:
------------------

- Slug added to be distinct and separate from Name
- Slug prefilled in Admin
- PublishedManager added for ease of use - QuickPages.objects.published


Future features / ToDo:
-----------------------

- Integrate menu handling / generation from slug/Name/Title
- Better Breadcrumb support
- Integrate w/keyedcache and/or memcache if present
- Dynamic template support
- Possible MarkDown / ReStructuredText / etc support
- Dynamic Site support (currently requires passing in the url declaration)
- Generic Meta-tag support (any meta tag, not just keywords & description

Send me a note or post a comment - this will influence what gets done first :)

j
