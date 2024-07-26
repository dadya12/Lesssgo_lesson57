from webapp.models import Task, Project
from webapp.forms import TaskForm
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'Task/task_detail.html'


class TaskCreateView(PermissionRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'Task/task_create.html'
    permission_required = 'webapp.add_task'

    def has_permission(self):
        projects = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        return super().has_permission() and self.request.user in projects.users.all()

    def form_valid(self, form):
        projects = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = projects
        task.save()
        form.save_m2m()
        return redirect('webapp:detail', pk=projects.pk)


class TaskEditView(PermissionRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'Task/task_update.html'
    permission_required = 'webapp.change_task'

    def has_permission(self):
        tag = self.get_object()
        return super().has_permission() and self.request.user in tag.project.users.all()

    def get_success_url(self):
        return reverse('webapp:task_detail', kwargs={'pk': self.object.pk})


class TaskDeleteView(PermissionRequiredMixin, DeleteView):
    model = Task
    template_name = 'Task/task_delete.html'
    permission_required = 'webapp.delete_task'

    def has_permission(self):
        tag = self.get_object()
        return super().has_permission() and self.request.user in tag.project.users.all()

    def get_success_url(self):
        return reverse('webapp:home')
