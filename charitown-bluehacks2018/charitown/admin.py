from django.contrib import admin
from charitown.models import Member, Community, Project, ProjectDonation
# Register your models here.

admin.site.register(Member)
admin.site.register(Community)
admin.site.register(Project)
admin.site.register(ProjectDonation)