import re
import json
import argparse
from datetime import datetime


def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def load_json(filepath, data):
    with open(file=filepath, mode='r', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print(f'Load JSON File')

def save_json(filepath, data):
    with open(file=filepath, mode='w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f'Save JSON File')
    
def convert_datetime(date):
    match = re.search(r"(\d+)月(\d+)日", date)
    if match:
        month, day = match.groups()
        date_formatted = f"{datetime.today().year}-{int(month):02d}-{int(day):02d}"
        
    return date_formatted
    
def convert_text_color(text, color='blue'):
    if color == 'red':
        return f'\033[31m{text}\033[0m'
    elif color == 'green':
        return f'\033[32m{text}\033[0m'
    elif color == 'yellow':
        return f'\033[33m{text}\033[0m'
    elif color == 'blue':
        return f'\033[34m{text}\033[0m'
    elif color == 'bright-yellow':
        return f'\033[93m{text}\033[0m'
    elif color == 'bright-blue':
        return f'\033[94m{text}\033[0m'

