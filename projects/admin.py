from django.contrib import admin

from projects.models import Project, Framework, Language, ProjectType, DevType, OngoingProjects, ProjectLevel, \
    RecruiterProject


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)


class FrameworkAdmin(admin.ModelAdmin):
    pass


admin.site.register(Framework, FrameworkAdmin)


class LanguageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Language, LanguageAdmin)


class ProjecttypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProjectType, ProjecttypeAdmin)


class DevtypeAdmin(admin.ModelAdmin):
    pass


@admin.register(ProjectLevel)
class ProjectLevelAdmin(admin.ModelAdmin):
    pass


@admin.register(OngoingProjects)
class OngoingProjectsAdmin(admin.ModelAdmin):
    pass


@admin.register(RecruiterProject)
class RecruiterProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(DevType, DevtypeAdmin)
