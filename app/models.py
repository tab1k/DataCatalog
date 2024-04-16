from django.db import models
from .information import *
from django.contrib.auth.models import User



class Passport(models.Model):

    name = models.CharField(max_length=255) # Наименованаие оргаанизации

    data_source = models.CharField(max_length=255, default="FRSP") # Наименоваание объекта информатизации осуществляющий сбор и обработку данных

    level_use_data = models.CharField(choices=LEVEL_USE_DATA_CHOICES, max_length=255) # Уровень межведомственного использоваания

    choice_type_data = models.CharField(choices=CHOICE_TYPE_DATA_CHOICES, max_length=255) # Способ введения данных

    data_type = models.CharField(choices=PERM_DATA_CHOICES, max_length=255) # Форма данных

    perm_data = models.CharField(choices=PERM_DATA_CHOICES, max_length=255) # Доступность данных

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_passports') # Владелец данных

    users = models.ManyToManyField(User, related_name='accessible_passports') # Пользователь данных

    npa = models.TextField() # Источник данных согласно НПА

    data_object = models.CharField(choices=DATA_OBJECT_CHOICES, max_length=255) # Объект описания

    period_update = models.CharField(choices=PERIOD_UPDATE_CHOICES, max_length=255) # Периодичность обновления

    graph_update = models.TextField(max_length=255) # График обновления

    len_update = models.TextField(max_length=255) # Порядок обновления

    npa_collection = models.TextField() # Перечень НПА регламинтирующий сбор и обработку

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Паспорт"
        verbose_name_plural = "Паспорты"


class PassportDataStructure(models.Model):

    passport = models.ForeignKey(to=Passport, on_delete=models.CASCADE)

    information_system_name = models.CharField(choices=INFORMATION_SYSTEM_CHOICES, max_length=255)

    bd_name = models.CharField(choices=BD_NAME_CHOICES, max_length=255)

    schema_name = models.CharField(max_length=255)

    table_name = models.CharField(max_length=255)

    table_description = models.TextField()

    table_type = models.CharField(max_length=255)

    column_id = models.IntegerField()

    column_name = models.CharField(max_length=255)

    column_type = models.CharField(max_length=255)

    column_description = models.TextField()

    reference_tbl_clmn = models.URLField(blank=True, null=True)

    flk = models.CharField(max_length=255)

    clmn_key_type = models.CharField(max_length=255)

    teg = models.CharField(max_length=255)

    def __str__(self):
        return self.table_name

    class Meta:
        verbose_name = "Описание структуры данных"
        verbose_name_plural = "Описание структуры данных"


class BusinessGlossary(models.Model):
    name = models.CharField(max_length=255)
    termin = models.TextField()
    national_name = models.TextField()
    alternative_name = models.TextField()
    acronym = models.TextField()
    abbreviation = models.TextField()
    previous_title = models.TextField()
    definition = models.TextField()
    definition_source = models.TextField()
    details = models.TextField()
    hyperlink = models.TextField()
    term_status = models.CharField(max_length=255, choices=TERM_STATUS_CHOICES)
    availability_of_the_term = models.BooleanField(default=False)
    passport_data_structure = models.ForeignKey(to=PassportDataStructure, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_availability_of_the_term(self):
        return "Да" if self.availability_of_the_term else "Нет"

    class Meta:
        verbose_name = "Бизнес Глоссарий"
        verbose_name_plural = "Бизнес Глоссарий"



