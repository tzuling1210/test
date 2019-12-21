from django.contrib import admin

from .models import Member

from import_export.admin import ImportExportModelAdmin

# Register your models here.
# admin.site.register(Member)
@admin.register(Member)
class MemberAdmin(ImportExportModelAdmin):
    list_display = ('id', 'member_name', 'age', 'gender', 'cellphone_number', 'email',  'dwelling')
