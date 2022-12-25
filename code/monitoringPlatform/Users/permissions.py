from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
 
# import User model
from Users.models import User
 
def addPermissionToGroup(groupName, permissionCodename, permissionName) :

    adminGroup, _ = Group.objects.get_or_create(name = groupName )

    ct = ContentType.objects.get_for_model(User)
 
    permission = Permission.objects.create(
        codename = permissionCodename, 
        name = permissionName,
        content_type = ct
    )

    adminGroup.permissions.add(permission)

addPermissionToGroup("admin", "authorize_registration_of_professional", "")