from django_filters import CharFilter, FilterSet
from .models import Post
from django import forms


class PostFilter(FilterSet):
    search_title = CharFilter(
        field_name='title',
        label='Post title',
        lookup_expr='icontains',
    )

