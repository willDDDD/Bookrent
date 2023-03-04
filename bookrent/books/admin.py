from django.contrib import admin

# Register your models here.
from .models import books
from .models import students


admin.site.register(books)
admin.site.register(students)