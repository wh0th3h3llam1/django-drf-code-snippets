'''
https://www.django-rest-framework.org/api-guide/pagination/
'''

from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):

    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'total': self.page.paginator.count,
            'page_size': self.get_page_size(request=self.request),
            'page': self.get_page_number(
                    request=self.request,
                    paginator=self.page.paginator
                ),
            'results': data
        })
