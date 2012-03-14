from django.contrib.localflavor.us.models import PhoneNumberField, USStateField
from django.db import models

class Person(models.Model):
	full_name = models.CharField(max_length=60)
	bio = models.CharField(max_length=500)
	phone_number = PhoneNumberField()
	email = models.EmailField()
	
	def __unicode__(self):
		return self.full_name
	
class Address(models.Model):
	street = models.CharField(max_length=200)
	city = models.CharField(max_length=17)
	state = USStateField()
	zip_code = models.CharField(max_length=10)
	
	def __unicode__(self):
		return "%s, %s, %s %s" % (self.street, self.city, self.state, self.zip_code)
	
class School(models.Model):
	institute = models.CharField(max_length=100)
	major = models.CharField(max_length=150)
	classification = models.CharField(max_length=40)
	grad_date = models.DateField()
	gpa = models.DecimalField(max_digits=4, decimal_places=2)
	icon = models.ImageField(upload_to='school_icons/')
	
	def __unicode__(self):
		return self.institute

class Description(models.Model):
	responsibilities = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.responsibilities

class Experience(models.Model):
	title = models.CharField(max_length=100)
	company = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	state = USStateField()
	start_date = models.DateField()
	end_date = models.DateField()
	descriptions = models.ManyToManyField(Description)
	
	def __unicode__(self):
		return "%s, %s" % (self.title, self.company)

class Extracurricular(models.Model):
	award_activity = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.award_activity

class Skill(models.Model):
	comp_skill = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.comp_skill

class Reference(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	job_position = models.CharField(max_length=100)
	company = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.name

class Resume(models.Model):
	title = models.CharField(max_length=50)
	person = models.ForeignKey(Person, related_name='resumes', null=False)
	address = models.ForeignKey(Address, null=True)
	schools = models.ManyToManyField(School)
	experiences = models.ManyToManyField(Experience)
	extracurriculars = models.ManyToManyField(Extracurricular)
	skills = models.ManyToManyField(Skill)
	references = models.ManyToManyField(Reference)
	
	def __unicode__(self):
		return self.title
