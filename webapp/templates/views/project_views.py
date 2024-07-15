from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View
from webapp.forms import TaskForm

from webapp.models import Task


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = Task.objects.all()
        return context


class DetailPageView(TemplateView):
    template_name = 'Project/detail.html'

    def get_context_data(self, **kwargs):
        task = get_object_or_404(Task, pk=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['task'] = task
        return context


class CreatePageView(View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'Project/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'Project/create.html', {'form': form})


class EditPageView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=self.kwargs['pk'])
        form = TaskForm(instance=task)
        return render(request, 'Project/update.html', {'form': form})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=self.kwargs['pk'])
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('detail', pk=task.id)
        else:
            return render(request, 'Project/update.html', {'form': form})


class DeletePageView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=self.kwargs['pk'])
        return render(request, 'Project/delete.html', {'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=self.kwargs['pk'])
        task.delete()
        return redirect('home')
