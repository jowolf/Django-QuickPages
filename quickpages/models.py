# encoding: utf-8

from django.db import models
#from django.utils.safestring import mark_safe

from taggit.managers import TaggableManager

#### Custom Managers

class PublishedManager (models.Manager):
    def published (self):
        return self.filter (published=True)

    def unpublished (self):
        return self.filter (published=False)


# This is specific to our site (eRacks.com), but here as an example for those who wish to use it:

class PRManager (models.Manager):
    def presspages (self):
        return self.filter (template__endswith="press.html").exclude (title__startswith='eRacks').order_by ('-created')


#### Models

class QuickPage (models.Model):
    slug        = models.CharField (max_length=1024, unique=True, help_text="This is the url. Slashes are OK, but not necessary.")
    name        = models.CharField (max_length=512, help_text="Name - short, typically one or two words.")
    title       = models.CharField (max_length=512, help_text="Page title, and optional H1 tag (see Heading)")
    published   = models.BooleanField (default=True, help_text="Published=shown. If not, gives 404")
    javascript  = models.CharField (max_length=1024, blank=True, help_text="Comma-separated filenames, relative to MEDIA_ROOT or STATIC_ROOT")
    css         = models.CharField (max_length=1024, blank=True, help_text="Comma-separated filenames, relative to MEDIA_ROOT or STATIC_ROOT")
    heading     = models.BooleanField (default=True, help_text='If "Heading" is checked, "Title" is added to the top of the content in an H1 tag.')
    meta_title  = models.CharField (max_length=512, blank=True, help_text="Meta title")
    description = models.TextField (blank=True, help_text="Meta description")
    keywords    = models.TextField (blank=True, help_text="Meta keywords")
    comments    = models.TextField (blank=True, help_text="Internal developer/editor comments, not shown")

    content     = models.TextField (blank=True,
                    help_text='HTML Content - main content div of the page.')
                    #help_text='HTML Content - <a href="javascript:mce_setup();">Click Here</a> to edit - see <a href="http://wiki.moxiecode.com/index.php/TinyMCE:Configuration">TinyMCE Configuration</a> for more options.')

    template    = models.CharField (max_length=100, blank=True,
                    help_text="Optional template - default is quickpages/base.html, which you can also simply replace in your project tree.")

    # site      = model.ForeignKey ('Site'...)

    updated     = models.DateTimeField ('date modified', auto_now=True)
    created     = models.DateTimeField ('date created', auto_now_add=True)

    objects     = PublishedManager()
    pr_objects  = PRManager()
    tags        = TaggableManager(blank=True)

    def get_absolute_url (self):
        return '/' + self.slug

    def __unicode__ (self):
        return self.name


types = (
    ('raw','Raw - passed thru as is'),
    ('html','HTML - Use the built-in HTML Editor (warning: will strip certain tags, etc'),
  )

class QuickSnippet (models.Model):
    name        = models.CharField(max_length=100, help_text="Name, identifier-style, no spaces, will be exported into request context")
    #slug       = models.CharField(max_length=100)
    title       = models.CharField(max_length=100, blank=True, help_text="Title, verbose name / short description")
    js          = models.TextField(blank=True, help_text="Javascript for this snippet - &lt;script&gt; tags will be passed through")
    css         = models.TextField(blank=True, help_text="CSS for this snippet - &lt;link&gt; tags will be passed through")
    #meta       = models.ManyToManyField (Meta, blank=True)
    body        = models.TextField(help_text="Body of snippet, available via {{ &lt;name&gt; }} in templates via context processor")
    comments    = models.TextField (blank=True, help_text="Internal developer/editor comments, not shown")
    typ         = models.CharField (max_length=20, default='raw', choices = types, help_text="Editor type - raw, html, etc - future: Markdown, etc")

    created     = models.DateTimeField('date created', auto_now_add=True)
    updated     = models.DateTimeField('date updated', auto_now=True)
    published   = models.BooleanField(default=True)

    objects     = PublishedManager()
    tags        = TaggableManager(blank=True)

    def __unicode__ (self):
        #return mark_safe (self.body or self.title or self.name)
        return '%s (%s)' % (self.name, self.title)


    # TODO:  Add template, image, possibly slug

    def get_absolute_url (self): return '/%s/' % self.name #slug
    url = property (get_absolute_url)

