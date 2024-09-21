# daily_reminder.py

# Get task description from the user
task = input("Enter your task: ")

# Get task priority
priority = input("Priority (high/medium/low): ").lower()

# Get time sensitivity information
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Customized reminder based on priority and time sensitivity
def create_reminder(task, priority, time_bound):
    match priority:
        case 'high':
            reminder = f"Reminder: Task: {task} is a HIGH priority task."
        case 'medium':
            reminder = f"Reminder: Task: {task} is a MEDIUM priority task."
        case 'low':
            reminder = f"Reminder: Task: {task} is a LOW priority task."
        case _:
            reminder = f"Reminder: Task: {task} has an UNKNOWN priority."

    # Modify the reminder if the task is time-sensitive
    if time_bound == 'yes':
        reminder += " It requires immediate attention today!"
    
    return reminder

# Generate and display the customized reminder
reminder_message = create_reminder(task, priority, time_bound)
print(reminder_message)
