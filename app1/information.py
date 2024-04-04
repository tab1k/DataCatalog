DATA_LEVEL_CHOICES = (
    ('republican', 'Республиканский'),
    ('local', 'Местный'),
    ('none', 'Данные на межведомственном уровне не используются'),
)

STORAGE_METHOD_CHOICES = (
    ('paper', 'В бумажном виде'),
    ('electronic', 'В электронном виде'),
    ('combined', 'Комбинированный'),
)

DATA_FORM_CHOICES = (
    ('primary', 'Первичные данные'),
    ('aggregated', 'Агрегированные данные'),
)

DATA_ACCESS_CHOICES = (
    ('limited', 'Ограниченный доступ'),
    ('unrestricted', 'Доступ без ограничений'),
)

DESCRIPTION_OBJECTS_CHOICES = (
    ('individuals', 'Физические лица'),
    ('legal_entities', 'Юридические лица'),
    ('property', 'Имущество'),
    ('results_of_work', 'Результаты работ'),
    ('intellectual_property', 'Охраняемые результаты интеллектуальной деятельности и приравненные к ним средства индивидуализации'),
    ('intangible_assets', 'Нематериальные блага'),
)