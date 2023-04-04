from django.contrib import admin
from annotator_app.models import Dataset, Text, Annotation

admin.site.register(Dataset)
admin.site.register(Text)
admin.site.register(Annotation)
