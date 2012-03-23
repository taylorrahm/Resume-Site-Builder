from resumes.models import Person, Resume, Address, School, Experience, \
						   Extracurricular, Description, Skill, Reference
from django.contrib import admin

class HiddenModelAdmin (admin.ModelAdmin):
	def get_model_perms(self, *args, **kwargs):
		perms = admin.ModelAdmin.get_model_perms(self, *args, **kwargs)
		perms['list_hide'] = True
		return perms

admin.site.register(Person)
admin.site.register(Resume)
admin.site.register(Address)
admin.site.register(School)
admin.site.register(Experience)
admin.site.register(Extracurricular)
admin.site.register(Description)
admin.site.register(Skill)
admin.site.register(Reference)
