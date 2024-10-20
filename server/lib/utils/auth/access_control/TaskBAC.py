#  Task-Based Access Control (TBAC)


# Define tasks and permissions
tasks = {
    'process_refund': ['modify_account', 'update_transaction'],
    'create_order': ['update_inventory', 'process_payment']
}

# Function to check if a user has permission based on their task
def check_task_permission(user_task, permission):
    if permission in tasks.get(user_task, []):
        return True
    return False

# Example
user_task = 'process_refund'
if check_task_permission(user_task, 'modify_account'):
    print("Access Granted")
else:
    print("Access Denied")
