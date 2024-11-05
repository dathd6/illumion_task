import random

def format_time(seconds):
    # Convert seconds to HH:MM:SS format
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours:02}:{minutes:02}:{secs:02}"

def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    # Format the color as a hexadecimal string
    return f'#{r:02X}{g:02X}{b:02X}'
