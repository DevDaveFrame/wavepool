from django.db import models

# Create your models here.


class Advertisement(models.Model):
    company_name = models.CharField(max_length=100)
    copy = models.TextField(null=False)
    # The following feels wrong, but matched the path for the current ads
    logo = models.ImageField(upload_to='static/spoonsers')
    url = models.URLField(blank=False, null=False)

    def __str__(self):
        return '<{}> {}'.format(self.company_name, self.copy[:20] + '...')
