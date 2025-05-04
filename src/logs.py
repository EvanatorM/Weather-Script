import os
from datetime import datetime

def log(message):
    os.makedirs("./logs", exist_ok=True)

    today = datetime.now()
    log_path = f"logs/log-{today.year}-{str(today.month).zfill(2)}.txt"
    message = f"[{str(today.month).zfill(2)}/{str(today.day).zfill(2)}/{today.year} {str(today.hour).zfill(2)}:{str(today.minute).zfill(2)}:{str(today.second).zfill(2)}] {message}"
    if (not message.endswith('\n')):
        message += '\n'

    with open(log_path, "a") as file:
        file.write(message)