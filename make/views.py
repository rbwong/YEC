from django.conf import settings
import os
from django.http import HttpResponseRedirect
from django.contrib.formtools.wizard.views import SessionWizardView
from django.core.files.storage import FileSystemStorage
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from make.models import Make



class IndexView(SessionWizardView, SuccessMessageMixin):
    template_name = 'index.html'
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'photos'))

    def done(self, form_list, **kwargs):
        messages.add_message(self.request, 20, "You have successfuly registered for YEC 2014 :)")
        new = Make()
        for form in form_list:
            for k,v in form.cleaned_data.iteritems():
                setattr(new, k, v)
        new.save()
        return HttpResponseRedirect('/#form')
