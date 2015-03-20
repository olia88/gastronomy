from django.contrib import admin
from recipes.models import Recipe, Comments

class CommentsInline(admin.StackedInline):
    model=Comments
    extra=1

class RecipeAdmin(admin.ModelAdmin):
    fields=['recipe_title', 'recipe_text', 'recipe_date', 'recipe_ingredients']
    inlines=[CommentsInline]
    list_filter=['recipe_date']


# Register your models here.
admin.site.register(Recipe, RecipeAdmin)