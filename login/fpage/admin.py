from django.contrib import admin
from .models import Detail

# Register your models here.
@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = True
    row_id_fields = ('name',)
    list_display = ('name', 'email', 'course', 'score',)

    list_filter = ('course', 'score',)

