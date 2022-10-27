from django.contrib import admin
# 导入model的BookInfo, PeopleInfo

from book.models import BookInfo, PeopleInfo

# Register your models here.

admin.site.register(BookInfo)
admin.site.register(PeopleInfo)
