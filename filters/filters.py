from django_filters import rest_framework as filters, CharFilter, DateFilter


# Create your filters here.


class MyModelFilterSet(filters.FilterSet):
    """
    Usage:

    ```
    from django_filters.rest_framework import DjangoFilterBackend
    from .filters import MyModelFilterSet


    class MyModelViewSet(ModelViewSet):
        ...
        filter_backends = (DjangoFilterBackend,)
        filterset_class = MyModelFilterSet
        ...
    ```
    """

    users = CharFilter(method="get_users")
    from_date = DateFilter(field_name="my_date_field", lookup_expr="gte")
    to_date = DateFilter(field_name="my_date_field", lookup_expr="lte")

    def get_users(self, queryset, key, value):
        """
        Filter comma-separated values
        """
        try:
            queryset = queryset.filter(users__in=value.split(","))
        except Exception:
            pass
        return queryset
