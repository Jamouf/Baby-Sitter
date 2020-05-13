def hours_worked(start_time, end_time):
    start_time = check_start_time(start_time)
    end_time = check_end_time(end_time)  
    return end_time - start_time

def check_start_time(start_time):
    if start_time < 17:
        start_time = 17
    return start_time

def check_end_time(end_time):
    if end_time not in range(12, 24 + 1):
        end_time = end_time + 24
    return end_time