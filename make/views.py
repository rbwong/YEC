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


'''
class SignupPage(SuccessMessageMixin, CreateView):
    model = Contact
    template_name = 'signup.html'
    success_message = "You have successfuly registered for Bloc Shot 2014 :)"

    def get_success_url(self):
        return reverse_lazy('signup_page')

    def get_context_data(self, **kwargs):
        context = super(SignupPage, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.designer = self.request.user
        return super(SignupPage, self).form_valid(form)

    def form_invalid(self, form):
        print form.errors
        return self.render_to_response(self.get_context_data(form=form))
'''
