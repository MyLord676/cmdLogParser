from datetime import datetime


def round_time_floor(time: datetime, minutesToRound=60):
    hour_in_seconds = 60 * minutesToRound
    return (time.timestamp() // hour_in_seconds) * hour_in_seconds
