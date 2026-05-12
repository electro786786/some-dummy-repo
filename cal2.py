import calendar

def get_calendar(year, month):
    try:
        cal = calendar.monthcalendar(year, month)
    except ValueError as e:
        print(f"Invalid date: {e}")
        return None
    return cal

# Example usage:
year = 2024
month = 9
print(get_calendar(year, month))