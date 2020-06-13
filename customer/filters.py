import django_filters
from . import models

class orderFilters(django_filters.FilterSet):
    class Meta:
        model = models.Order
        feilds = "__all__"
        exclude = ['date_created']
        exclude = ['customer','user']