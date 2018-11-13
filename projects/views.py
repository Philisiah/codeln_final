from django.shortcuts import render

from projects.models import Project, Projecttype, Devtype


# Create your views here.
# def project_categories(request):
#     # list all project categories
#     if request.method == 'GET':
#         return render(request, 'projects/categories.html', {})
#     elif request.method == 'POST':
#         return HttpResponse('<h2> Done </h2>')


# def project_category_list(request):
#     # list all project from above category
#     # filter projects by framework, language
#     pass


def project_list(request, id):
    # TODO: filter projects by framework, language and category using django filter
    categoryname = Projecttype.objects.get(id=id)

    projecttypes = Project.objects.filter(projecttype_id=id)
    return render(request, 'projects/all_projects.html', {'projecttypes': projecttypes, 'categoryname': categoryname})


def devtypes_view(request, id):
    devtype = Devtype.objects.get(id=id)
    projects = Project.objects.filter(devtype=devtype)
    return render(request, 'projects/devtypes.html', {'projects': projects, 'devtype': devtype})


def projecttypes_view(request, id):
    projecttype = Projecttype.objects.get(id=id)
    projects = Project.objects.filter(projecttype=projecttype)
    return render(request, 'projects/projecttype.html', {'projects': projects, 'projecttype': projecttype})


def categories(request):
    projecttypes = Projecttype.objects.all()
    devtypes = Devtype.objects.all()

    return render(request, 'projects/categories.html', {'projecttypes': projecttypes, 'devtypes': devtypes})


def project(request, id):
    project = Project.objects.get(id=id)
    return render(request, 'projects/project.html', {'project': project})
