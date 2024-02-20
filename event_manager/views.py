from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters import rest_framework as filters

from .models import Event
from .serializers import EventSerializer


class IsSuperUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated

        if request.method == 'PUT' or request.method == 'PATCH':
            return request.user == view.get_object().user

        return False


class BasePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'pageSize'


class EventFilter(filters.FilterSet):
    date_before = filters.DateFilter(field_name='date', lookup_expr='gte')
    date_after = filters.DateFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Event
        fields = {
            'date': ['range'],
        }


class EventViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperUserOrReadOnly]
    queryset = Event.objects.all().order_by('-id')
    serializer_class = EventSerializer
    pagination_class = BasePagination
    filter_backends = [SearchFilter, OrderingFilter, filters.DjangoFilterBackend]
    filterset_class = EventFilter
    search_fields = ['name', 'location', 'description']
    ordering_fields = '__all__'

