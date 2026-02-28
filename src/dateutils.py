from datetime import datetime

def today_key() -> str:
    return datetime.now().strftime('%Y-%m-%d')
