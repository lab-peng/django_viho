import os
from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    code = models.CharField(max_length=10, unique=True)
    state = models.CharField(max_length=10, default='Active')
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.code

class ProjectFile(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    file = models.FileField(upload_to='project_files')

    class Meta:
        ordering = ('-id',)

    @property
    def filename(self):
        return os.path.basename(self.file.name)
