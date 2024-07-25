from django.db.models import Q
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import ProjectForm, SearchForm, ProjectUserForm
from webapp.models import Project
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class HomePageView(ListView):
    model = Project
    template_name = 'Project/home.html'
    context_object_name = 'projects'
    paginate_by = 5

    def dispatch(self, request, *args, **kwargs):
        self.search_form = SearchForm(request.GET)
        self.search_value = None
        if self.search_form.is_valid():
            self.search_value = self.search_form.cleaned_data['search']
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(name__icontains=self.search_value) | Q(description__icontains=self.search_value))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.search_form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search_value'] = self.search_value
        return context


class DetailPageView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'Project/detail.html'


class CreatePageView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'Project/create.html'
    form_class = ProjectForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        form.instance.users.add(self.request.user)
        return response

    def get_success_url(self):
        return reverse('webapp:detail', kwargs={'pk': self.object.pk})


class EditPageView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'Project/update.html'

    def get_success_url(self):
        return reverse('webapp:detail', kwargs={'pk': self.object.pk})


class DeletePageView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'Project/delete.html'
    success_url = reverse_lazy('webapp:home')


class UpdateUserView(UpdateView):
    model = Project
    form_class = ProjectUserForm
    template_name = 'update_user.html'
    context_object_name = 'projects'
    permission_required = 'auth.change_user'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('webapp:detail', kwargs={'pk': self.object.pk})
