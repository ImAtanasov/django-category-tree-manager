from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category, CategorySimilarity

'''
Inline editing allows you to edit related objects on the same page as the parent object, which can be very convenient for managing related data.
'''


class CategorySimilarityInline(admin.TabularInline):
    model = CategorySimilarity  # Specifies that this inline interface is for the CategorySimilarity model.
    extra = 1  # Specifies that one extra empty form should be displayed for adding new CategorySimilarity instances.
    fk_name = 'category_a'  # Specifies that the foreign key to use for this inline interface is category_a.


class CategoryAdmin(MPTTModelAdmin):
    list_display = ('name', 'parent', 'description', 'image')
    search_fields = ('name',)
    list_filter = ('parent',)
    fields = ('name', 'description', 'image', 'parent')
    actions = ['delete_selected']
    inlines = [CategorySimilarityInline]  # Add inline editing


admin.site.register(Category, CategoryAdmin)


class CategorySimilarityAdmin(admin.ModelAdmin):
    list_display = ('category_a', 'category_b')
    search_fields = ('category_a__name', 'category_b__name')
    list_filter = ('category_a__name', 'category_b__name')
    fields = ('category_a', 'category_b')
    actions = ['delete_selected']


admin.site.register(CategorySimilarity, CategorySimilarityAdmin)
