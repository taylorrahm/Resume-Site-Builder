from django.template import Context, loader
from django.http import HttpResponse
from resumes.models import Resume

def main(request):
	resume = Resume.objects.all()[0]
	t = loader.get_template('resume.html')
	c = Context({
			'resume': resume,
	})
	return HttpResponse(t.render(c))
	
