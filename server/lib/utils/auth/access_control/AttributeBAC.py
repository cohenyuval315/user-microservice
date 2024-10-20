# Attribute-Based Access Control 

def can_access(user, resource, action):
    if user.department == resource.required_department and user.location == resource.allowed_location:
        return True
    return False