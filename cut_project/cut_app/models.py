from django.db import models
from django.utils.crypto import get_random_string
from cut_app.make_cut import cut

# Create your models here.

class Links(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=7, default=cut)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.short_url