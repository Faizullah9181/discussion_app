from rest_framework.pagination import PageNumberPagination


class PollPaginator(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page_no"