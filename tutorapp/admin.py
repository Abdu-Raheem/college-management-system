from django.contrib import admin

from .models import TutorStudents, TutorSubjects

admin.site.register(TutorStudents)
admin.site.register(TutorSubjects)
