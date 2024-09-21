# daily_reminder.py

# Get task description from the user
task = input("Enter the task description: ")

# Get task priority
priority = input("Enter the task priority (high, medium, low): ").lower()

# Get time sensitivity information
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Customized reminder based on priority and time sensitivity
def create_reminder(task, priority, time_bound):
    match priority:
        case 'high':
            reminder = f"Task: {task} is a HIGH priority task."
        case 'medium':
            reminder = f"Task: {task} is a MEDIUM priority task."
        case 'low':
            reminder = f"Task: {task} is a LOW priority task."
        case _:
            reminder = f"Task: {task} has an UNKNOWN priority."

    # Modify the reminder if the task is time-sensitive
    if time_bound == 'yes':
        reminder += " It requires immediate attention today!"
    
    return reminder

# Generate and display the customized reminder
reminder_message = create_reminder(task, priority, time_bound)
print(reminder_message)
