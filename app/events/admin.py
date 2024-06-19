from django.contrib import admin
from .models import Category, Event, Tag, PDFMOdel, MachineType, MachineTypeFile

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

class MachineTypeFileInline(admin.TabularInline):
    model = MachineTypeFile
    extra = 1


@admin.register(MachineType)
class MachineTypeAdmin(admin.ModelAdmin):
    inlines = [MachineTypeFileInline]


@admin.register(PDFMOdel)
class PDFAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "updated_at"]
    list_display_links = ["id", "name"]  # was ist anklickbar?


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "date", "author", "category", "is_active"]
    list_display_links = ["id", "name"]