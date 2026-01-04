from django.contrib import admin


from .models import EnrolledSubject, ExamResult

admin.site.register(EnrolledSubject)
admin.site.register(ExamResult)