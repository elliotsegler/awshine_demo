from __future__ import unicode_literals
from django.core.files.storage import default_storage

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages

from django.shortcuts import get_object_or_404  

from django.conf import settings

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest


#from .forms import ContactForm, FilesForm, ContactFormSet

from .models import Feedback
from .forms import FeebackForm


# logging...
import logging
logger = logging.getLogger(__name__)


# http://yuji.wordpress.com/2013/01/30/django-form-field-in-initial-data-requires-a-fieldfile-instance/
class FakeField(object):
    storage = default_storage


fieldfile = FieldFile(None, FakeField, 'dummy.txt')

# Create your views here.

def is_debug(context):
	context['debug'] = settings.DEBUG
	#logger.error('Debug: ' + str(settings.DEBUG))
	return context

class HomePageView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        #messages.info(self.request, 'This is a demo of a message.')
        #context['ingredients'] = Ingredient.objects.all()
        form = FeebackForm()
        context = is_debug(context)
        context['form'] = form
        return context


def FeedbackFormView(request):
    if request.method == 'POST':
        form = FeebackForm(request.POST)
        logger.debug(str(form.is_valid()))
        if (form.is_valid()):
            feedback = Feedback(name=form.cleaned_data['name'],email=form.cleaned_data['email'],rating=form.cleaned_data['rating'],feedback=form.cleaned_data['feedbackText'])
            feedback.save()
            return HttpResponse('OK')
        else:
            return HttpResponseBadRequest()
    else:
        return HttpResponseRedirect('/')