def hours_worked(start_time, end_time):  
    if start_time < 17:
        start_time = 17
    return end_time - start_time