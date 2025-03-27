import time

def log(message):
    print(f"[LOG] {time.strftime('%Y-%m-%d %H:%M:%S')} - {message}")

def rate_limit(limit: int, time_window: int):
    pass
