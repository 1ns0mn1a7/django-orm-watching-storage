SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // SECONDS_IN_HOUR
    minutes = (total_seconds % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE
    return f"{hours}ч {minutes}мин"
