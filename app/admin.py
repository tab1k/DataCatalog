from .models import *
from django.contrib import admin


class PassportAdmin(admin.ModelAdmin):
    list_display = ['name', 'data_source', 'level_use_data', 'choice_type_data', 'data_type', 'perm_data', 'created_at', 'updated_at']  # Отображаемые поля в списке записей
    list_filter = ['level_use_data', 'choice_type_data', 'data_type', 'perm_data', 'created_at', 'updated_at']  # Фильтры для списка записей
    search_fields = ['name', 'data_source', 'npa', 'data_object', 'graph_update', 'len_update', 'npa_collection']  # Поля для поиска
    ordering = ['-created_at']  # Сортировка записей по умолчанию


class PassportDataStructureAdmin(admin.ModelAdmin):
    list_display = ['passport', 'information_system_name', 'bd_name', 'schema_name', 'table_name', 'table_type', 'column_id', 'column_name', 'column_type']  # Отображаемые поля в списке записей
    list_filter = ['information_system_name', 'bd_name', 'schema_name', 'table_name', 'table_type']  # Фильтры для списка записей
    search_fields = ['passport__name', 'table_description', 'column_name', 'column_description']  # Поля для поиска
    ordering = ['-passport__name']  # Сортировка записей по умолчанию


class BusinessGlossaryAdmin(admin.ModelAdmin):
    list_display = ['name', 'termin', 'national_name', 'alternative_name', 'acronym', 'abbreviation', 'previous_title', 'definition', 'definition_source']  # Отображаемые поля в списке записей
    list_filter = ['name', 'termin', 'national_name', 'alternative_name', 'acronym']  # Фильтры для списка записей
    search_fields = ['name', 'termin', 'term_status', 'availability_of_the_term']  # Поля для поиска
    ordering = ['-name']  # Сортировка записей по умолчанию


admin.site.register(BusinessGlossary, BusinessGlossaryAdmin)
admin.site.register(PassportDataStructure, PassportDataStructureAdmin)
admin.site.register(Passport, PassportAdmin)