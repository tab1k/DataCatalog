from django.contrib import admin
from .models import AttributeData, DigitalData, ReferenceInfo


admin.site.register(DigitalData)
admin.site.register(AttributeData)
admin.site.register(ReferenceInfo)