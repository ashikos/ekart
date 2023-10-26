from django.db import models
from django.conf import settings



class AbstractbaseModel(models.Model):
    """ model to store basic detals of objects

    Atribs:
        creator(obj): Creator of the object
        updater(obj): Updater of the object
        created_on(datetime): Added date of the object
        updated_on(datetime): Last updated date of the object
    """

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, default=None, null=True,
        blank=True, related_name="creator_%(class)s_objects",
        on_delete=models.SET_NULL)
    updater = models.ForeignKey(
        settings.AUTH_USER_MODEL, default=None, null=True,
        blank=True, related_name="updater_%(class)s_objects",
        on_delete=models.SET_NULL)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True  # model is not meant to be instantiated directly. It is to be  used as a base class for other models.
