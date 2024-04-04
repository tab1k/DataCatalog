from django.db import models

from .information import *


class Organization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DataPassport(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    object_name = models.CharField(max_length=255)

    DATA_LEVEL = models.CharField(max_length=50, choices=DATA_LEVEL_CHOICES)

    storage_method = models.CharField(max_length=50, choices=STORAGE_METHOD_CHOICES)

    data_form = models.CharField(max_length=50, choices=DATA_FORM_CHOICES)

    data_access = models.CharField(max_length=50, choices=DATA_ACCESS_CHOICES)

    users_according_to_npa = models.TextField()
    data_source_according_to_npa = models.TextField()
    actual_data_sources = models.TextField()

    description_objects = models.CharField(max_length=50, choices=DESCRIPTION_OBJECTS_CHOICES)
    update_frequency = models.CharField(max_length=255)
    update_schedule = models.CharField(max_length=255)
    update_order = models.CharField(max_length=255)
    npa_list_for_data_collection_and_processing = models.TextField()
    npa_list_for_data_entry_and_consumption = models.TextField()
    npa_list_for_data_entry_and_consumption_restrictions = models.TextField()
    data_class = models.CharField(max_length=255)
    creation_date = models.DateField()

    def __str__(self):
        return self.object_name

    class Meta:
        verbose_name = "Паспорт данных"
        verbose_name_plural = "Паспорт данных"
