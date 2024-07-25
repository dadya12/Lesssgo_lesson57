from django import forms
from webapp.models import Task, Project


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'type', 'status']
        widgets = {'type': forms.CheckboxSelectMultiple}


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'created_date', 'updated_date']
        widgets = {
            'created_date': forms.SelectDateWidget,
            'updated_date': forms.SelectDateWidget
        }


class ProjectUserForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['users']
        widgets = {'users': forms.CheckboxSelectMultiple}


class SearchForm(forms.Form):
    search = forms.CharField(max_length=150, required=False, label='Search')
