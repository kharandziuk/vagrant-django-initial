from django.views.generic import TemplateView

from celery import debug_task

class HelloView(TemplateView):
    template_name = 'hello.html'

    def get_context_data(self):
        debug_task()
        #assert False
