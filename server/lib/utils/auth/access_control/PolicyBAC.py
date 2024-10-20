# Policy-Based Access Control (PBAC)
 
# Define policies
policies = [
    {'role': 'admin', 'action': 'delete', 'resource': 'user'},
    {'role': 'user', 'action': 'read', 'resource': 'document'},
]

# Function to evaluate policies
def evaluate_policies(user, action, resource):
    for policy in policies:
        if user['role'] == policy['role'] and action == policy['action'] and resource == policy['resource']:
            return True
    return False

# Example evaluation
user = {'role': 'admin'}
if evaluate_policies(user, 'delete', 'user'):
    print("Access Granted")
else:
    print("Access Denied")
