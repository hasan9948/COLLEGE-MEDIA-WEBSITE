from django.contrib import admin
from miniprojectapp.models import academictable,culturaltable,eventstable,nsstable,placementstable,sportstable,rightmsgtable

class academicadmin(admin.ModelAdmin):
    list_display=('title','description','image','datetime','type')
class rightmsgtablea(admin.ModelAdmin):
    list_display=('name',)

admin.site.register(academictable,academicadmin)
admin.site.register(culturaltable)
admin.site.register(eventstable)
admin.site.register(placementstable)
admin.site.register(nsstable)
admin.site.register(sportstable)
admin.site.register(rightmsgtable,rightmsgtablea)
# Register your models here.