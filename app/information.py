

# Passport

LEVEL_USE_DATA_CHOICES = (
    ('republic', 'Республиканский'),
    ('local', 'Местный'),
    ('nonused', 'Данные на межведомственном уровне не используются'),
)

CHOICE_TYPE_DATA_CHOICES = (
    ('paper', 'В бумажном виде'),
    ('digital', 'В электронном виде'),
    ('combine', 'Комбинированный'),
)

DATA_TYPE_CHOICES = (
    ('pervak', 'Первичные данные'),
    ('vtoryak', 'Агрегированные данные'),
)

PERM_DATA_CHOICES = (
    ('private', 'Ограниченный доступ'),
    ('public', 'Доступ без ограничений'),
)

DATA_OBJECT_CHOICES = (
    ('individuals', 'Физические лица'),
    ('legal', 'Юридические лица'),
    ('property', 'Имущество'),
)

PERIOD_UPDATE_CHOICES = (
    ('', 'Не установлена'),
    ('', 'По мере необходимости'),
    ('', 'По мере поступления данных'),
    ('', 'Непрерывное обновление'),
    ('', 'Установлена НПА'),
)

INFORMATION_SYSTEM_CHOICES = (
    ('mob_depart', 'Информационная система "Мобильное правительство"'),
)

BD_NAME_CHOICES = (
    ('postgresql', 'PostgreSQL'),
    ('mysql', 'MySQL'),
    ('sqlite3', 'SQLite3'),
    ('oracle', 'Oracle'),
    ('firebase', 'Firebase'),
)

TERM_STATUS_CHOICES = (
    ('valid', 'Действующий'),
    ('invalid', 'Не действующий'),
)

FREQUENCY_CHOICES = (
    ('monthly', 'ежемесячная'),
    ('quarterly', 'ежеквартальная'),
    ('semi', 'полугодичная'),
)

SECTOR_CHOICES = (
    ('bvu', 'БВУ'),
    ('so', 'СО'),
    ('rcb', 'РЦБ'),
    ('mfo', 'МФО')
)

