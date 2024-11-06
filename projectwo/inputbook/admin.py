# inputbook/admin.py
from django.contrib import admin
from .models import Book

class RatingClassificationFilter(admin.SimpleListFilter):
    title = 'clasificación de valoración'
    parameter_name = 'rating_classification'

    def lookups(self, request, model_admin):
        return [
            ('baja', 'Baja'),
            ('media', 'Media'),
            ('alta', 'Alta'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'baja':
            return queryset.filter(rating__lt=1000)
        elif self.value() == 'media':
            return queryset.filter(rating__gte=1000, rating__lte=2500)
        elif self.value() == 'alta':
            return queryset.filter(rating__gt=2500)
        return queryset

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rating', 'rating_classification', 'fecha_creacion', 'fecha_modificacion')
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    list_filter = ('rating', 'fecha_modificacion', RatingClassificationFilter)  # Incluye el filtro personalizado
    search_fields = ('title', 'author')