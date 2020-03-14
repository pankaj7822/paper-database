from django.contrib import admin
from .models import paper
# Register your models here.

@admin.register(paper)
class paperAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "year",
        "id_no",
        "pattern",
        "level",
        "language",
        "testtype",
        "is_test_added",
        "is_solution_added",
    )
    list_display_links = ("id", "year","id_no")
    list_filter = ("pattern", "level", "language","testtype","is_test_added","is_solution_added","year")


