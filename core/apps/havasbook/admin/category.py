from django.contrib import admin
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin


from ..models import CategoryModel


@admin.register(CategoryModel)
class CategoryAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id",
        "name",
    )
    
    search_fields = ['name']  # yoki o'zingizning modelingizdagi qidiriladigan maydon
