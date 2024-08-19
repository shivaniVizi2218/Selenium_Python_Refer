import random
import string
from datetime import datetime, timedelta
import os
import subprocess

def generate_random_string(length):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def add_days_current_date(format="%m/%d/%Y" , days_to_add=1):
    new_date = (datetime.now() + timedelta(days=days_to_add)).strftime(format)
    return new_date

def delete_all_files_from_downloads():
    file_path = os.path.abspath('.') + "\\Downloads"
    if os.path.isdir(file_path):
        for filename in os.listdir(os.path.abspath('.') + "\\Downloads"):
            if os.path.isfile(os.path.join(os.path.abspath('.') + "\\Downloads", filename)):
                os.remove(os.path.join(os.path.abspath('.') + "\\Downloads", filename))

def change_system_time_zone(time_zone):
    command_to_execute = 'TZUTIL /s "' + time_zone + '"'
    os.system(command_to_execute)

def get_system_time_zone():
    result = subprocess.run(['tzutil', '/g'], capture_output=True, text=True)
    return result.stdout.strip()
def previous_day_current_date(format="%m/%d/%Y", days_to_subtract=1):
    new_date = (datetime.now() - timedelta(days=days_to_subtract)).strftime(format)
    return new_date


def previous_day_current_date(format="%m/%d/%Y", days_to_subtract=1):
    new_date = (datetime.now() - timedelta(days=days_to_subtract)).strftime(format)
    return new_date
