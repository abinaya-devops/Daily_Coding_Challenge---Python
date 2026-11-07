from datetime import datetime

def get_weekday(date_string):
    date = datetime.strptime(date_string, "%Y-%m-%d")
    weekday = date.strftime("%A")
    return weekday
