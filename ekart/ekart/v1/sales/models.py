from django.db import models
from common.models import AbstractbaseModel
from v1.sales.constants import *

# Create your models here.


class Category(AbstractbaseModel):
    """ model to store product categories"""

    type = models.IntegerField(
        default=Categories.CLOTHING, choices=Categories.choices())
    description = models.TextField(null=True, blank=True)