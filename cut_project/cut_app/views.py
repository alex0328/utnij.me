import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from cut_app import models
from cut_app import forms

# Create your views here.

class Index_View(View):
    def get(self, request):
        if request.is_ajax():
            request_getdata = request.GET.get('form_value')
            add_cut = models.Links(original_url=request_getdata)
            add_cut.save()
            cut_url_ready = '{}/{}'.format(request.META['HTTP_HOST'], add_cut)
            ctx = {'cut_url_ready': cut_url_ready}
            return HttpResponse(json.dumps(ctx))
        else:
            form = forms.Link_form
            ctx = {"form": form}
            return render(request, 'cut_app/index.html', ctx)

    @csrf_exempt
    def post(self, request):
        print("nie jestem ajaxem")
        form = forms.Link_form(request.POST)
        if form.is_valid():
            cut_url = form.save(commit=False)
            form.save()
            cut_url_ready = '{}/{}'.format(request.META['HTTP_HOST'], cut_url)
            ctx = {'cut_url_ready': cut_url_ready}
        return render(request, 'cut_app/index.html', ctx)

class Redirect_me_View(View):
    def get(self, request, short_url):
        print(short_url)
        try:
            url_record = models.Links.objects.get(short_url=short_url)
        except:
            form = forms.Link_form
            ctx = {'short_url': short_url,
                   'form': form}
            return render(request, 'cut_app/index.html', ctx)
        return HttpResponseRedirect(url_record.original_url)
