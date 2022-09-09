from rest_framework.pagination import PageNumberPagination
from rest_framework.settings import api_settings
from rest_framework.response import Response


class PageNumberWithLimitPagination(PageNumberPagination):
    page_size = api_settings.PAGE_SIZE or 15
    page_size_query_param = 'limit'
    max_page_size = 100
    total_pages = 0
    per_page = 0


    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'total_pages': self.page.paginator.num_pages,
            'per_page': len(self.page.object_list),
            'page': self.page.number,
            'results': data
        })
