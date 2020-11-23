from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from django.http import JsonResponse

from django.urls import reverse

from django.utils.crypto import get_random_string

from shortener.models import UrlObject

from shortener.exceptions import UrlAlreadyExistsException


class UrlObjectListView(ListView):

    model = UrlObject
    template_name = "shortener/list.html"


class UrlObjectCreateView(CreateView):

    model = UrlObject
    template_name = "shortener/create.html"
    fields = ['long_url', 'short_url']

    def get_success_url(self):
        return reverse('list_view')

    def form_valid(self, form):

        instance = form.instance

        if not instance.short_url:

            generated_url = get_random_string(10)

            while UrlObject.objects.filter(short_url=generated_url):

                generated_url = get_random_string(10)

            instance.short_url = f'http://localhost:8000/{generated_url}'

        else:

            generated_url = f'http://localhost:8000/{instance.short_url}'

            if UrlObject.objects.filter(short_url=generated_url).exists():

                raise UrlAlreadyExistsException('Please choose another name. This one is already taken')

            instance.short_url = generated_url

        self.object = form.save()

        return super().form_valid(form)


def increase_visitors_counter(request, *args, **kwargs):

    if request.is_ajax:

        url_id = request.GET['url_id']

        url_object = UrlObject.objects.filter(pk=url_id).first()

        url_object.visits += 1
        url_object.save()

        return JsonResponse({'visits': url_object.visits})
