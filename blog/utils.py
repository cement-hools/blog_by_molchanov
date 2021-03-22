from django.shortcuts import get_object_or_404, render, redirect

from .models import *


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        obj_name_in_context = self.model.__name__.lower()
        context = {
            obj_name_in_context: obj,
        }
        return render(request, self.template, context)


class ObjectCreateMixin:
    model_form = None
    template = None

    def get(self, request):
        form = self.model_form()
        context = {
            'form': form,
        }
        return render(request, self.template, context)

    def post(self, request):
        bound_form = self.model_form(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        context = {
            'form': bound_form,
        }
        return render(request, self.template, context)
