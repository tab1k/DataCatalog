from django.db import models

from .information import *


class Organization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_full_info(self):
        organization_data_passports = self.datapassport_set.all()
        full_info = f'Organization Name: {self.name}\n'
        for passport in organization_data_passports:
            full_info += f'Object Name: {passport.object_name}\n'
            full_info += f'Data Level: {passport.DATA_LEVEL}\n'
            full_info += f'Storage Method: {passport.storage_method}\n'
            full_info += f'Data Form: {passport.data_form}\n'
            full_info += f'Data Access: {passport.data_access}\n'
            full_info += f'Users According to NPA: {passport.users_according_to_npa}\n'
            full_info += f'Data Source According to NPA: {passport.data_source_according_to_npa}\n'
            full_info += f'Actual Data Sources: {passport.actual_data_sources}\n'
            full_info += f'Description Objects: {passport.description_objects}\n'
            full_info += f'Update Frequency: {passport.update_frequency}\n'
            full_info += f'Update Schedule: {passport.update_schedule}\n'
            full_info += f'Update Order: {passport.update_order}\n'
            full_info += f'NPA List for Data Collection and Processing: {passport.npa_list_for_data_collection_and_processing}\n'
            full_info += f'NPA List for Data Entry and Consumption: {passport.npa_list_for_data_entry_and_consumption}\n'
            full_info += f'NPA List for Data Entry and Consumption Restrictions: {passport.npa_list_for_data_entry_and_consumption_restrictions}\n'
            full_info += f'Data Class: {passport.data_class}\n'
            full_info += f'Creation Date: {passport.creation_date}\n\n'
        return full_info

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"


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
