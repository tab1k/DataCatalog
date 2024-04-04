from django.db import models
from .information import *


class DigitalData(models.Model):
    type_data_object = models.CharField(choices=TYPE_OF_DATA, max_length=255)
    name_data_object = models.CharField(choices=NAME_DATA_OBJECT, max_length=255)
    description_data_object = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.type_data_object} {self.name_data_object}'

    def get_full_info(self):
        attribute_data_list = self.attributedata_set.all()
        reference_info_list = self.referenceinfo_set.all()

        full_info = f'{self.type_data_object} {self.name_data_object} {self.description_data_object}\n'

        for attribute_data in attribute_data_list:
            full_info += f'Данные атрибута: {attribute_data.last_name} {attribute_data.first_name} {attribute_data.num_doc}\n'

        for reference_info in reference_info_list:
            full_info += f'Справочная информация: {reference_info.info}\n'

        return full_info

    class Meta:
        verbose_name = 'Цифровые данные'
        verbose_name_plural = 'Цифровые данные'


class AttributeData(models.Model):
    digital_data = models.ForeignKey(DigitalData, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    third_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(choices=GENDER_DATA_OBJECT, max_length=255)
    num_doc = models.BigIntegerField(blank=False, null=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.digital_data} {self.num_doc}'

    class Meta:
        verbose_name = 'Данные атрибута'
        verbose_name_plural = 'Данные атрибутов'


class ReferenceInfo(models.Model):
    digital_data = models.ForeignKey(DigitalData, on_delete=models.CASCADE)
    info = models.TextField()

    def __str__(self):
        max_length = 50
        truncated_info = self.info[:max_length] + ('...' if len(self.info) > max_length else '')
        return f'{self.digital_data} {truncated_info}'

    class Meta:
        verbose_name = 'Справочная информация'
        verbose_name_plural = 'Справочные информации'

