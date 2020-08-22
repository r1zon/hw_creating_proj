from django.contrib import admin

from table.models import Table, Savepath


class TableAdmin(admin.ModelAdmin):
    pass

class SavepathAdmin(admin.ModelAdmin):
    pass


admin.site.register(Table, TableAdmin)
admin.site.register(Savepath, SavepathAdmin)
