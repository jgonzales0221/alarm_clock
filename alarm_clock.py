def alarm_clock():
    # Get current time and wait duration from user
    current_hours = int(input("Enter the current time (hours, 0-23): "))
    current_minutes = int(input("Enter the current time (minutes, 0-59): "))
    wait_hours = int(input("Enter the number of hours to wait: "))
    wait_minutes = int(input("Enter the number of minutes to wait: "))

    # Convert current time and wait time to total minutes
    current_total_minutes = current_hours * 60 + current_minutes
    wait_total_minutes = wait_hours * 60 + wait_minutes

    # Calculate the alarm time in total minutes
    alarm_total_minutes = (current_total_minutes + wait_total_minutes) % 1440  # 1440 minutes in a day

    # Convert the alarm time back to hours and minutes
    alarm_hours = alarm_total_minutes // 60
    alarm_minutes = alarm_total_minutes % 60

    # Output result
    print(f"The alarm will go off at {alarm_hours:02d}:{alarm_minutes:02d}")

# Run the function
alarm_clock()