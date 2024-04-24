from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from .serializers import *
from itertools import chain
from django.db.models import Q, Value, CharField, F
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from .models import Passport, PassportDataStructure, BusinessGlossary
from .serializers import SearchResultsSerializer


class CustomPagination(PageNumberPagination):
    page_size = 10


class PassportViewSet(viewsets.ModelViewSet):
    queryset = Passport.objects.select_related('owner').all()
    serializer_class = PassportSerializer
    pagination_class = CustomPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        sector = self.request.query_params.get('sector', None)
        queryset = Passport.objects.select_related('owner')
        if sector:
            queryset = queryset.filter(sector=sector)
        return queryset


class PassportDetailAPIView(RetrieveUpdateAPIView):
    queryset = Passport.objects.select_related('owner').all()
    serializer_class = PassportSerializer


class PassportDataStructureViewSet(viewsets.ModelViewSet):
    queryset = PassportDataStructure.objects.all()
    serializer_class = PassportDataStructureSerializer
    permission_classes = [AllowAny]


class BusinessGlossaryViewSet(viewsets.ModelViewSet):
    queryset = BusinessGlossary.objects.all()
    serializer_class = BusinessGlossarySerializer
    permission_classes = [AllowAny]


class SearchResultsAPIView(ListAPIView):
    serializer_class = SearchResultsSerializer

    def get_queryset(self):
        query = self.request.query_params.get('search', '')

        # Filter passports
        passports = Passport.objects.filter(
            Q(name__icontains=query) | Q(owner__username__icontains=query)
        ).annotate(
            model_name=Value('Passport', output_field=CharField()),
            model_id=F('id')
        )

        # Filter passport data structures
        structures = PassportDataStructure.objects.filter(
            table_name__icontains=query
        ).annotate(
            model_name=Value('PassportDataStructure', output_field=CharField()),
            model_id=F('id')
        )

        # Filter business glossaries
        glossaries = BusinessGlossary.objects.filter(
            Q(name__icontains=query) | Q(termin__icontains=query)
        ).annotate(
            model_name=Value('BusinessGlossary', output_field=CharField()),
            model_id=F('id')
        )

        # Combine and return the results
        return list(chain(passports, structures, glossaries))




















