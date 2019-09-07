from django_filters import rest_framework as filters
from .models import Borrowed

class BorrowedFilterSet(filters.FilterSet):
    # Format
    # ['exact', 'lte', 'gte', 'isnull']
    missing = filters.BooleanFilter(field_name='returned', lookup_expr='isnull')

    class Meta:
        model = Borrowed
        fields = ['what','to_who', 'missing']