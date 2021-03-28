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
            'admin_object': obj,
            'detail': True,
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


class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        obj_name_in_context = self.model.__name__.lower()
        context = {
            'form': bound_form,
            obj_name_in_context: obj,
        }
        return render(request, self.template, context)

    def post(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        bound_form = self.model_form(request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)

        obj_name_in_context = self.model.__name__.lower()
        context = {
            'form': bound_form,
            obj_name_in_context: obj,
        }
        return render(request, self.template, context)


class ObjectDelete:
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug=slug)
        obj_name_in_context = self.model.__name__.lower()
        context = {
            obj_name_in_context: obj,
        }
        return render(request, self.template, context)

    def post(self, request, slug):
        obj = self.model.objects.get(slug=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))
