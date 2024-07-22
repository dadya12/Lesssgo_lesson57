from webapp.models import Task, Project
from webapp.forms import TaskForm
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect, reverse


class TaskDetailView(DetailView):
    model = Task
    template_name = 'Task/task_detail.html'


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'Task/task_create.html'

    def form_valid(self, form):
        projects = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = projects
        task.save()
        form.save_m2m()
        return redirect('webapp:detail', pk=projects.pk)


class TaskEditView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'Task/task_update.html'

    def get_success_url(self):
        return reverse('webapp:task_detail', kwargs={'pk': self.object.pk})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'Task/task_delete.html'

    def get_success_url(self):
        return reverse('webapp:home')
