from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from itertools import chain
from .serializers import *
from .permissions import *
from django.db.models import Q, F
from rest_framework.filters import SearchFilter


class PassportViewSet(viewsets.ModelViewSet):
    queryset = Passport.objects.all()
    serializer_class = PassportSerializer
    permission_classes = [AllowAny]


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
    filter_backends = [SearchFilter]
    search_fields = ['name', 'owner__username', 'passportdatastructure__passport__name', 'passportdatastructure__table_name', 'businessglossary__name', 'businessglossary__termin']

    def get_queryset(self):
        query = self.request.query_params.get('search', '')

        # Create an empty queryset
        queryset = Passport.objects.none()

        # Filter passports
        passports = Passport.objects.filter(name__icontains=query).annotate(
            name_annotated=F('name'),
            owner_annotated=F('owner__username')
        ).values('name_annotated', 'owner_annotated')

        # Filter passport data structures
        structures = PassportDataStructure.objects.filter(table_name__icontains=query).annotate(
            passport_annotated=F('passport__name'),
            table_name_annotated=F('table_name')
        ).values('passport_annotated', 'table_name_annotated')

        # Filter business glossaries
        glossaries = BusinessGlossary.objects.filter(name__icontains=query).annotate(
            name_annotated=F('name'),
            termin_annotated=F('termin')
        ).values('name_annotated', 'termin_annotated')

        # Combine querysets
        for passport in passports:
            queryset |= Passport.objects.filter(name=passport['name_annotated'], owner__username=passport['owner_annotated'])

        for structure in structures:
            queryset |= PassportDataStructure.objects.filter(passport__name=structure['passport_annotated'], table_name=structure['table_name_annotated'])

        for glossary in glossaries:
            queryset |= BusinessGlossary.objects.filter(name=glossary['name_annotated'], termin=glossary['termin_annotated'])

        return queryset.distinct()




















