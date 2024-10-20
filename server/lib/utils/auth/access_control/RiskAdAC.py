# Risk-Adaptive Access Control (RAdAC)


# Function to calculate risk level
def calculate_risk(user, action):
    if user['is_vpn'] == False and action == 'delete':
        return 'high'
    return 'low'

# Function to allow access based on risk
def allow_access(risk):
    if risk == 'low':
        return True
    return False

# Example evaluation
user = {'is_vpn': False}
action = 'delete'
risk = calculate_risk(user, action)
if allow_access(risk):
    print("Access Granted")
else:
    print("Access Denied")
