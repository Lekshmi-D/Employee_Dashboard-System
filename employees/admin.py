from django.contrib import admin
from .models import Member, Task , Managers
from django.contrib.auth.models import User

# Register your models here.
"""
@admin.register(Member)
class MemberModel(admin.ModelAdmin):
    readonly_fields = ('firstname' , "lastname",'position','salary','work_hours')

    def get_readonly_fields(self,request,obj):
        
        #get_user = User.objects.filter(is_superuser=True)
        #get_user = self.model.objects.all()
        get_user=self.model.objects.filter(test=True)

        #get_users = User.objects.all()
        #for user in get_user:
      #if user.is_superuser == True:
        # print(get_user.firstname,obj.firstname)
"""

admin.site.register(Member)
admin.site.register(Task)
admin.site.register(Managers)