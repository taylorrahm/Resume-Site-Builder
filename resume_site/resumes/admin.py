from resumes.models import Person, Resume, Address, School, Experience, \
						   Extracurricular, Description, Skill, Reference
from django.contrib import admin

class HiddenModelAdmin (admin.ModelAdmin):
	def get_model_perms(self, *args, **kwargs):
		perms = admin.ModelAdmin.get_model_perms(self, *args, **kwargs)
		perms['list_hide'] = True
		return perms

admin.site.register(Person, HiddenModelAdmin)
admin.site.register(Resume)
admin.site.register(Address, HiddenModelAdmin)
admin.site.register(School, HiddenModelAdmin)
admin.site.register(Experience, HiddenModelAdmin)
admin.site.register(Extracurricular, HiddenModelAdmin)
admin.site.register(Description, HiddenModelAdmin)
admin.site.register(Skill, HiddenModelAdmin)
admin.site.register(Reference, HiddenModelAdmin)
