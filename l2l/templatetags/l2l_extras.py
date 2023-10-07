from django import template
from datetime import datetime

register = template.Library()


@register.filter
def l2l_dt(value):
    # If it's already a datetime, format it
    if isinstance(value, datetime):
        return value.strftime('%Y-%m-%d')

    # If it's a string, parse and format it
    try:
        parsed_date = datetime.fromisoformat(value)
        return parsed_date.strftime('%Y-%m-%d')
    except ValueError as e:
        print(f"Error parsing date: {e}")
        return value  # Return original if can't be parsed
