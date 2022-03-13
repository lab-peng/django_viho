import os

from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from .models import Project, ProjectFile
from .forms import ProjectFileForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template.defaultfilters import filesizeformat

def index(request):
    return render(request, 'index.html')

def dropzone(request):
    return render(request, 'dropzone.html')

def file_manager(request):
    return render(request, 'file-manager.html')

def bootstrap_border_table(request):
    context = {
        'project_list': Project.objects.all()
    }
    return render(request, 'bootstrap-border-table.html', context)

def base_input(request):
    return render(request, 'base-input.html')

class ProjectList(ListView):
    model = Project
    


def project_update(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'POST':
        project_file_form = ProjectFileForm(request.POST, request.FILES)
        if project_file_form.is_valid():
            print(request.FILES.getlist('file'))
            file = project_file_form.save(commit=False)
            file.project = project
            file.save()
            data = {'is_valid': True, 'name': file.filename, 'url': file.file.url, 'size': filesizeformat(file.file.size)}
        else:
            print(project_file_form.errors)
            data = {'is_valid': False}
        print(data)
        return JsonResponse(data)

    project_file_form = ProjectFileForm()
    context = {
        'project': project,
        'project_file_form': project_file_form,
    }
    return render(request, 'a/project_update_form.html', context)

def delete_project_file(request):
    project_file_pk = request.POST.get('project_file_pk')
    project_file = get_object_or_404(ProjectFile, pk=project_file_pk)
    project_file.file.delete()
    project_file.delete()
    response = {
        'message': 'success'
    }
    return JsonResponse(response)


# plan A
# get the deleted object and then remove the li element
# maybe I need to put pk inside the li element first, it's unique and easy to find

# plan B
# get project_file.project.projectfile_set.all().values('filename', 'url', 'size')
# or construct a list of dicts like above and return a JsonResponse(List)
# in the template , in the ajax success callback function, paste the list inside ul






