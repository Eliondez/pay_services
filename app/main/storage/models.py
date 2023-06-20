from django.db import models
from django.utils.text import slugify


class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='protected')

    def __str__(self):
        return self.title

    @property
    def true_link(self):
        print(1111, self.file.url)
        return 'ololo'

    # @property
    # def pretty_name(self):
    #     return "{0}.{1}".format(slugify(self.title), '111')
                # get_extension(self.file.name))
