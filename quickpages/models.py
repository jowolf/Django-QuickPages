# encoding: utf-8

from django.db import models


class PublishedManager (models.Manager):
    def published (self):
        return self.filter (published=True)

    def unpublished (self):
        return self.filter (published=False)


class PRManager (models.Manager):
    def presspages (self):
        return self.filter (template__endswith="press.html").exclude (title__startswith='eRacks').order_by ('-created')


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

    def get_absolute_url (self):
        return '/' + self.slug

    def __unicode__ (self):
        return self.name


